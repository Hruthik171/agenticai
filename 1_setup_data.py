"""
Setup and load financial statement data.
Computes YoY/QoQ deltas and key financial KPIs.
"""

import pandas as pd
import numpy as np
from pathlib import Path
import json
from typing import Dict, List, Tuple

class FinancialDataProcessor:
    """Process financial statements and compute KPIs."""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        self.statements = {}
        self.kpis = {}
    
    def load_sample_data(self) -> pd.DataFrame:
        """
        Load or create sample financial data.
        In production, this would load from SEC EDGAR or Kaggle.
        """
        # Sample data structure: balance sheet, income statement, cash flow
        sample_income_stmt = {
            'Quarter': ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023', 'Q1 2024', 'Q2 2024'],
            'Revenue': [45000, 48500, 52000, 58000, 62000, 67500],
            'COGS': [18000, 19400, 20800, 23200, 24800, 27000],
            'Operating_Expense': [12000, 13000, 14000, 15000, 16000, 17500],
            'Net_Income': [12000, 13500, 14700, 16800, 18200, 20100],
            'EPS': [0.50, 0.56, 0.61, 0.70, 0.76, 0.84],
        }
        
        sample_balance_sheet = {
            'Quarter': ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023', 'Q1 2024', 'Q2 2024'],
            'Total_Assets': [500000, 520000, 545000, 580000, 605000, 635000],
            'Total_Liabilities': [200000, 210000, 220000, 235000, 245000, 260000],
            'Shareholders_Equity': [300000, 310000, 325000, 345000, 360000, 375000],
            'Current_Ratio': [1.8, 1.85, 1.9, 1.95, 1.98, 2.0],
        }
        
        sample_cash_flow = {
            'Quarter': ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023', 'Q1 2024', 'Q2 2024'],
            'Operating_Cash_Flow': [10000, 11500, 12800, 15000, 16200, 18000],
            'Investing_Cash_Flow': [-3000, -3500, -4000, -5000, -5500, -6000],
            'Financing_Cash_Flow': [2000, 1500, 1000, 500, 0, -1000],
        }
        
        self.statements['income'] = pd.DataFrame(sample_income_stmt)
        self.statements['balance'] = pd.DataFrame(sample_balance_sheet)
        self.statements['cashflow'] = pd.DataFrame(sample_cash_flow)
        
        return self.statements
    
    def compute_yoy_qoq_deltas(self) -> Dict[str, pd.DataFrame]:
        """Compute Year-over-Year and Quarter-over-Quarter changes."""
        deltas = {}
        
        for stmt_name, df in self.statements.items():
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            delta_df = df[['Quarter']].copy()
            
            for col in numeric_cols:
                # QoQ % change
                delta_df[f'{col}_QoQ_%'] = df[col].pct_change() * 100
                # Absolute change
                delta_df[f'{col}_QoQ_abs'] = df[col].diff()
            
            deltas[f'{stmt_name}_qoq'] = delta_df
        
        return deltas
    
    def compute_kpis(self) -> Dict[str, float]:
        """Compute key financial KPIs."""
        kpis = {}
        
        income = self.statements['income']
        balance = self.statements['balance']
        cashflow = self.statements['cashflow']
        
        # Use latest quarter data
        latest_idx = -1
        
        # Profitability metrics
        kpis['Gross_Margin_%'] = ((income.loc[latest_idx, 'Revenue'] - income.loc[latest_idx, 'COGS']) 
                                   / income.loc[latest_idx, 'Revenue'] * 100)
        kpis['Operating_Margin_%'] = ((income.loc[latest_idx, 'Revenue'] - income.loc[latest_idx, 'COGS'] 
                                       - income.loc[latest_idx, 'Operating_Expense']) 
                                      / income.loc[latest_idx, 'Revenue'] * 100)
        kpis['Net_Margin_%'] = (income.loc[latest_idx, 'Net_Income'] / income.loc[latest_idx, 'Revenue'] * 100)
        
        # Leverage & Liquidity
        kpis['Debt_to_Equity'] = (balance.loc[latest_idx, 'Total_Liabilities'] 
                                  / balance.loc[latest_idx, 'Shareholders_Equity'])
        kpis['Current_Ratio'] = balance.loc[latest_idx, 'Current_Ratio']
        kpis['ROE_%'] = (income.loc[latest_idx, 'Net_Income'] 
                         / balance.loc[latest_idx, 'Shareholders_Equity'] * 100)
        
        # Growth metrics (YoY from 4 quarters ago if available)
        if len(income) >= 5:
            revenue_growth = ((income.loc[latest_idx, 'Revenue'] - income.iloc[-5, 'Revenue']) 
                             / income.iloc[-5, 'Revenue'] * 100)
            kpis['YoY_Revenue_Growth_%'] = revenue_growth
        
        self.kpis = kpis
        return kpis
    
    def export_analysis(self, output_file: str = "financial_analysis.json"):
        """Export statements and KPIs to JSON."""
        export_data = {
            'statements': {k: v.to_dict() for k, v in self.statements.items()},
            'kpis': self.kpis
        }
        
        output_path = self.data_dir / output_file
        with open(output_path, 'w') as f:
            json.dump(export_data, f, indent=2, default=str)
        
        print(f"✓ Analysis exported to {output_path}")
        return output_path


if __name__ == "__main__":
    processor = FinancialDataProcessor()
    
    print("📊 Loading financial statements...")
    processor.load_sample_data()
    
    print("📈 Computing KPIs...")
    kpis = processor.compute_kpis()
    print("\nKey Financial KPIs:")
    for k, v in kpis.items():
        print(f"  {k}: {v:.2f}")
    
    print("\n📉 Computing YoY/QoQ deltas...")
    deltas = processor.compute_yoy_qoq_deltas()
    
    print("\n💾 Exporting analysis...")
    processor.export_analysis()
    
    print("\n✅ Data setup complete!")
