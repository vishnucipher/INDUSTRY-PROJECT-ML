#### This is the ML project which in the industry level based

```
logs_path = os.path.join(os.getcwd(),'logs')

os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,'LOG')

logging.basicConfig(filename=LOG_FILE_PATH,format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
level=logging.INFO,)

```
