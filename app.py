from flask import Flask, render_template ,request
import pandas as pd
import datetime

app = Flask(__name__)

@app.route('/', methods=['get'])
def show_index():
  return render_template('daily-check.html', title = '検温でーす')


@app.route('/result', methods=['POST'])
def add_entry():
  df = pd.read_csv('static/BodyTemp_data.csv',index_col=0)

  Datetime = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
  Date = Datetime.date()
  Jcode = request.form.get('jcode')
  Temp = request.form.get('temp')
  df.loc[str(Date),str(Jcode)]=round(float(Temp),1)
  df.to_csv('static/BodyTemp_data.csv')
  df_columns = df.columns.tolist()
  df_columns.insert(0,'date')
  df_values = df.values.tolist()
  df_index = df.index.tolist()
  return render_template('result.html', title='{}さんの送信を受け付けました！'.format(Jcode), df_columns=df_columns, df_values=df_values, df_index=df_index)

@app.route('/view_logs', methods=['post','get'])
def view_logs():
  df = pd.read_csv('static/BodyTemp_data.csv',index_col=0)
  df_columns = df.columns.tolist()
  df_columns.insert(0,'date')
  df_values = df.values.tolist()
  df_index = df.index.tolist()
  return render_template('view_logs.html', title='履歴を見る画面どすえ', df_columns=df_columns, df_values=df_values, df_index=df_index)

if __name__ == '__main__':
  app.run(debug=True)
