import pandas as pd

class ExcelHandler:
    def __init__(self, filepath):
        self.filepath = filepath
    
    def load_data(self):
        try:
            df = pd.read_excel(self.filepath)
            
            required_columns = ['ФИО студента', 'Группа', 'Математика', 'Физика', 'Информатика']
            
            for col in required_columns:
                if col not in df.columns:
                    raise ValueError(f'Отсутствует обязательный столбец: {col}')
            
            return df
            
        except Exception as e:
            raise Exception(f'Ошибка при загрузке файла: {str(e)}')
    
    def save_result(self, dataframe, output_path):
        try:
            dataframe.to_excel(output_path, index=False)
        except Exception as e:
            raise Exception(f'Ошибка при сохранении файла: {str(e)}')
