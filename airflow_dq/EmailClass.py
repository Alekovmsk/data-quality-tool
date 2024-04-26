class EmailBody:
    def __init__(self, dqi):
        self.subject = f"По контролю качества данных {str(dqi)} (Self-Service DQ)"
        self.html_content = f"""<font face="sans-serif">
        Добрый день!
        В рамках процесса обеспечения качества данных по контролю {str(dqi)} обнаружены ошибки.
        <br>
        <a href = "https://ord-d12ell:5555/dq_report/{str(dqi)}" target = "_blank">Результат</a>&emsp;&emsp;'
        <a href = "https://ord-d12ell:5555/spec?uk={str(dqi)}" target = "_blank">Информация о контроле</a></font>"""
