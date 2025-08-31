import pandas as pd
from IPython.display import display, HTML

def pprint_pandas(*ser_dfs):
    """在 Jupyter Notebook 中一行并排打印多个 DataFrame 或 Series"""
    df_htmls = []
    for idx, ser_df in enumerate(ser_dfs, start=1):
        if isinstance(ser_df, pd.Series):
            name = ser_df.name if ser_df.name else f"<SERIES {idx}>"
            df_html = pd.DataFrame(ser_df, columns=[name])._repr_html_()
        elif isinstance(ser_df, pd.DataFrame):
            df_html = ser_df._repr_html_()
        else:
            raise TypeError(f"Unsupported type: {type(ser_df)}, value must be a `Series` or a `DataFrame`")
        df_htmls.append(df_html)
    side_by_side_html = f"""
        <div style="display: flex;">
            {"\n".join(f'<div style="margin-right: 20px;">{df_html}</div>' for df_html in df_htmls)}
        </div>
    """
    display(HTML(side_by_side_html))