from flask import Flask, render_template, request, send_file
import os
import pandas as pd
from excel_handler import ExcelHandler
from student_processor import StudentProcessor

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    try:
        if 'file' not in request.files:
            return 'Ошибка: Файл не загружен', 400
        
        file = request.files['file']
        
        if file.filename == '':
            return 'Ошибка: Файл не выбран', 400
        
        if not file.filename.endswith('.xlsx'):
            return 'Ошибка: Файл должен быть в формате .xlsx', 400
        
        try:
            threshold = float(request.form.get('threshold', 4.0))
        except ValueError:
            return 'Ошибка: Некорректное значение порога', 400
        
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        
        handler = ExcelHandler(filepath)
        df = handler.load_data()
        
        processor = StudentProcessor(df)
        result_df = processor.process(threshold)
        
        output_path = 'report.xlsx'
        handler.save_result(result_df, output_path)
        
        return send_file(
            output_path,
            as_attachment=True,
            download_name='report.xlsx'
        )
        
    except Exception as e:
        return f'Ошибка обработки: {str(e)}', 500

if __name__ == '__main__':
    app.run(debug=True)
