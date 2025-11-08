from flask import Flask, render_template, jsonify
import sqlite3
import os
from datetime import datetime, timedelta
import yfinance as yf

app = Flask(__name__)

# データベースファイルのパス（相対パスで取得）
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
DB_PATH = os.path.join(project_root, 'db', 'BS_DB.db')

print(f"データベースパス: {DB_PATH}")


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/companies')
def get_companies():
    """全社名リストを取得"""
    conn = get_db_connection()
    companies = conn.execute('''
        SELECT DISTINCT CompanyName, Code 
        FROM BS 
        WHERE Code IS NOT NULL
        ORDER BY CompanyName
    ''').fetchall()
    conn.close()

    return jsonify([{
        'name': company['CompanyName'],
        'code': company['Code']
    } for company in companies])


@app.route('/api/company/<code>')
def get_company_by_code(code):
    """証券コードで会社を検索"""
    conn = get_db_connection()

    company = conn.execute('''
        SELECT DISTINCT CompanyName, Code 
        FROM BS 
        WHERE Code = ?
        LIMIT 1
    ''', (code,)).fetchone()
    conn.close()

    if company:
        return jsonify({
            'name': company['CompanyName'],
            'code': company['Code']
        })
    else:
        return jsonify({'error': 'Company not found'}), 404


@app.route('/api/stock-price/<code>')
def get_stock_price(code):
    """株価データを取得"""
    try:
        # 日本株の証券コード（.Tを付ける）
        ticker = f"{code}.T"
        stock = yf.Ticker(ticker)

        # 過去10年分のデータを取得
        end_date = datetime.now()
        start_date = end_date - timedelta(days=10 * 365)
        hist = stock.history(start=start_date, end=end_date)

        if hist.empty:
            return jsonify({'error': 'No stock data found'}), 404

        # データを整形
        stock_data = []
        for index, row in hist.iterrows():
            stock_data.append({
                'date': index.strftime('%Y-%m-%d'),
                'close': float(row['Close'])
            })

        return jsonify(stock_data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/bs-data/<company_name>')
def get_bs_data(company_name):
    """特定の会社のBSデータを取得"""
    conn = get_db_connection()
    bs_data = conn.execute('''
        SELECT 
            EndDay,
            Assets,
            NetAssets,
            Equity,
            CurrentAssets,
            CashAndDeposits,
            CashAndCashEquivalent,
            PropertyPlantAndEquipment,
            RetainedEarnings,
            AccountingStandard,
            FinancialReportType
        FROM BS 
        WHERE CompanyName = ?
        ORDER BY EndDay
    ''', (company_name,)).fetchall()
    conn.close()

    return jsonify([{
        'date': row['EndDay'],
        'assets': row['Assets'],
        'netAssets': row['NetAssets'],
        'equity': row['Equity'],
        'currentAssets': row['CurrentAssets'],
        'cashAndDeposits': row['CashAndDeposits'],
        'cashAndCashEquivalent': row['CashAndCashEquivalent'],
        'propertyPlantAndEquipment': row['PropertyPlantAndEquipment'],
        'retainedEarnings': row['RetainedEarnings'],
        'accountingStandard': row['AccountingStandard'],
        'financialReportType': row['FinancialReportType']
    } for row in bs_data])


if __name__ == '__main__':
    # データベースの存在確認
    if os.path.exists(DB_PATH):
        print(f"データベースが見つかりました: {DB_PATH}")
        app.run(debug=True, port=5001)  # ポート5001で起動（既存アプリと競合しないように）
    else:
        print(f"エラー: データベースが見つかりません: {DB_PATH}")