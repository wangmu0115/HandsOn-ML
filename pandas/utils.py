from IPython.display import display, HTML
import pandas as pd

def pprint_series(*sers):
    """在 Jupyter Notebook 中一行并排打印多个 Series"""
    sers_html = "\n".join(f'<div style="margin-right: 20px;">{pd.DataFrame(ser, columns=["series"+str(idx)])._repr_html_()}</div>' for idx, ser in enumerate(sers, start=1))
    side_by_side_html = f"""
    <div style="display: flex;">
        {sers_html}
    </div>
    """
    display(HTML(side_by_side_html))

def pprint_dataframes(*dfs):
    """在 Jupyter Notebook 中一行并排打印多个 DataFrame"""
    dfs_html = "\n".join(f'<div style="margin-right: 20px;">{df._repr_html_()}</div>' for df in dfs)
    side_by_side_html = f"""
    <div style="display: flex;">
        {dfs_html}
    </div>
    """
    display(HTML(side_by_side_html))
    

def pprint_pds(*ser_dfs):
    """在 Jupyter Notebook 中一行并排打印多个 Series 或者 DataFrame"""
    pd_htmls = []
    for idx, ser_df in enumerate(ser_dfs, start=1):
        if isinstance(ser_df, pd.Series):
            pd_html = pd.DataFrame(ser_df, columns=["SERIES" + str(idx)])._repr_html_()
        elif isinstance(ser_df, pd.DataFrame):
            pd_html = ser_df._repr_html_()
        else:
            raise TypeError(f"不支持的数据类型: {type(ser_df)}")
        pd_htmls.append(pd_html)
    side_by_side_html = f"""
    <div style="display: flex;">
        {"\n".join(f'<div style="margin-right: 20px;">{pd_html}</div>' for pd_html in pd_htmls)}
    </div>
    """
    display(HTML(side_by_side_html))