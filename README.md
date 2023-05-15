# Examples-autotests-web-grid
Для запуска окружения используйте: \
`docker-compose up --build -d` \
`pip install -r requirements.txt`

### Для запуска тестов используйте:
`pytest -sv --alluredir=allure_folder --fib=10 ` \
Где `--fib` номер числа Фибоначчи

### Также можно использовать: 
--browser_name - имя браузера \
--browser_version - версия браузера \
--url - адрес Grid

### Для сборки отчета allure используйте:
`allure serve allure_folder`

### Для просмотра выполнения теста можно использовать:
http://localhost:7900/?autoconnect=1&resize=scale&password=secret \
или \
http://localhost:7902/?autoconnect=1&resize=scale&password=secret