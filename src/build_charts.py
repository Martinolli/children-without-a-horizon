import plotly.express as px
import pandas as pd

def build_education_chart(csv_path, out_html):
    df = pd.read_csv(csv_path)
    edu_inds = ["Literacy (Grade 2)", "Children in Poverty (0–14)", "Primary Education Spending"]
    df_edu = df[df['Indicator'].isin(edu_inds)]
    fig = px.bar(df_edu, x="Indicator", y="Value", color="Country", barmode="group")
    fig.write_html(out_html)
    print(f"Chart saved to {out_html}")

if __name__ == "__main__":
    build_education_chart("../data/raw/child_indicators.csv", "../dashboards/education_auto.html")
