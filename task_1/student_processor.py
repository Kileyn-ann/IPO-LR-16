import pandas as pd

class StudentProcessor:
    def __init__(self, dataframe):
        self.df = dataframe.copy()
    
    def calculate_average(self):
        subjects = ['Математика', 'Физика', 'Информатика']
        self.df['Средний балл'] = self.df[subjects].mean(axis=1).round(2)
    
    def filter_by_threshold(self, threshold):
        return self.df[self.df['Средний балл'] >= threshold]
    
    def add_scholarship_type(self, dataframe):
        dataframe['Тип стипендии'] = dataframe['Средний балл'].apply(
            lambda x: 'Повышенная' if x == 5.0 else 'Обычная'
        )
        return dataframe
    
    def process(self, threshold):
        self.calculate_average()
        filtered_df = self.filter_by_threshold(threshold)
        result_df = self.add_scholarship_type(filtered_df)
        return result_df
