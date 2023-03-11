import datetime
from apps import download, get_file_name, get_url


def test_apps_download(mocker):
    
    mocker.patch("requests.get", return_value = True)
    html = download('https://casas.mitula.com.co/searchRE/nivel3-Chapinero/nivel2-Bogot%C3%A1/nivel1-Cundinamarca/tipo-Casa/q-Bogot%C3%A1-Chapinero')
    
    assert html 

def test_apps_get_file_name(): 
    now = datetime.datetime.now()
    file_name = now.strftime("%Y-%m-%d") + ".html"
    
    assert  get_file_name() == file_name


def test_apps_get_url():
    assert  get_url() == 'https://casas.mitula.com.co/searchRE/nivel3-Chapinero/nivel2-Bogot%C3%A1/nivel1-Cundinamarca/tipo-Casa/q-Bogot%C3%A1-Chapinero'
    