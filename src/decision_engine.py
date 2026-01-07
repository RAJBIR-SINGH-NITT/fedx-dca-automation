import pandas as pd
import numpy  as np
def run_decision_engine():
        data = pd.read_csv("data/overdue_cases.csv")
        print(data.head())

            
        risk_map = {
                "high": "High",
                "HIGH": "High",
                "MEDIUM": "Medium",
                "LOW": "Low",
                "NORMAL": "Low"
             }

        data["customer_risk"] = data["customer_risk"].map(risk_map)

            
        data["region"] = data["region"].str.replace("DCA_", "", regex=False)
        data["region"] = data["region"].str.title()
            
        print("\nCleaned Data:")
        print(data.head())


            
        risk_score_map = {
                "Low": 0.3,
                "Medium": 0.6,
                "High": 1.0
            }

        data["risk_score"] = data["customer_risk"].map(risk_score_map)

            
        data["amount_score"] = data["invoice_amount"] / data["invoice_amount"].max()


    
        data["overdue_score"] = data["days_overdue"] / data["days_overdue"].max()

        data["priority_score"] = (
        0.4 * data["amount_score"] +
        0.4 * data["overdue_score"] +
        0.2 * data["risk_score"]
       )
        
        def priority_label(score):
            if score >= 0.7:
                 return "High"
            elif score >= 0.4:
                 return "Medium"
            else:
                 return "Low"

        data["priority_level"] = data["priority_score"].apply(priority_label)


        print("\nFinal Priority Output:")
        print(
        data[
            [
                "case_id",
                "invoice_amount",
                "days_overdue",
                "customer_risk",
                "region",
                "priority_score",
                "priority_level",
            ]
        ]
    )
        
        
        dca_data = pd.read_csv("data/dca_performance.csv")

        dca_data["dca_score"] = (
    
             0.5 * dca_data["recovery_rate"] +
             0.3 * dca_data["sla_compliance"] -
             0.2 * (dca_data["avg_recovery_time"] / dca_data["avg_recovery_time"].max())
    )
        

        best_dca_map = (
        dca_data
        .sort_values("dca_score", ascending=False)
        .set_index("dca_name")["dca_score"]
    )

        
        data["recommended_dca"] = data["region"].apply
        (
        lambda r: f"DCA_{r.upper()}"
    )
        

        final_output = data[
        [
            "case_id",
            "invoice_amount",
            "days_overdue",
            "customer_risk",
            "priority_level",
            "recommended_dca"
        ]
    ]

        
        final_output.to_csv("output/python_output.csv", index=False)

        
        
        print("\nFinal Output Saved to output/python_output.csv")
        
        
        
        print(final_output)









