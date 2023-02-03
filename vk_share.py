#import vk_api
import vk
import json
import time
import subprocess
import sys



# process output with an API in the subprocess module:
reqs = subprocess.check_output([sys.executable, '-m', 'pip',
'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
#print(installed_packages)
if "'vk'" not in installed_packages:
  print('vk is apsent, installing..')
  # implement pip as a subprocess:
  subprocess.check_call([sys.executable, '-m', 'pip', 'install',
  'vk'])
s_login = '+79870848106'
s_pass ='@gC=cB,r)BK,G64'
s_appid = '51541407'
s_key = 'f4d1bda5f4d1bda5f4d1bda5f7f7c3c83aff4d1f4d1bda5970ad41a242e9ad858671016'
k_data = 'data'

m_data = []

#vk = vk.DirectUserAPI(user_login=s_login, user_password=s_pass, scope='messages',v='5.131')
#vk = vk.API(session)
#vk_session = vk_api.VkApi(s_login, s_pass)
#vk_session.auth()

#vk = vk_session.get_api()

#print(vk.wall.post(message='Hello world!'))
#f_groups = vk.groups.get()
#print(f_groups)
#result = vk.wall.post(owner_id="-"+str(f_groups['items'][0]),message="Просто текст...!!!!!!!!!!!!!!!!!!!!!!!")
#print(result)

def get_data():
    try:
        f = open(k_data, 'r')
    except FileNotFoundError as e:
        print('no data yet')
        return 0
    fData = False
    try:
        fData = json.load(f)
    except ValueError as e:
        print('chat data still empty')
        return 0
    m_chat = fData
    print(f'load data:\n{m_chat}')
    f.close()
    return m_chat

def set_data(f_param):
    try:
        f = open(k_data, 'r')
    except FileNotFoundError as e:
        f = open(k_data, 'x')
        f = open(k_data, 'r')
    fData = False
    try:
        fData = json.load(f)
    except ValueError as e:
        print('chat data still empty')
    f.close()
    if (fData):
        for q_key in f_param.keys():
            fData[q_key] = f_param[q_key]
    else:
        fData = f_param

    fData = json.dumps(fData)
    with open(k_data, "w") as my_file:
        my_file.write(fData)
        my_file.close()
    print(fData)

def add_acc():
  f_log = input('Введите логин\n>>')
  f_pass = input('Введите пароль\n>>')
  try:
    f_res = vk.DirectUserAPI(user_login=f_log,user_password=f_pass, scope='messages',v='5.131')
  except Exception as e:
    print(e)
    return

  #print(f_res)
  m_data.append({'login':f_log,'pass':f_pass})
  set_data({'users': m_data})
  print('Учетная запись добавлена')

def list_acc():
  for q in m_data:
    print(q['login'])

def start_spam():
  f_msg = input('Напишите сообщение для рассылки\n>>')
  f_photo = input('Напишите адрес фото (вида photo124324_35345)\n>>')
  f_pause = int(input('Напишите паузу между постами, в секундах\n>>'))
  print('Рассылка запущена\n\nДЛЯ ПРЕРЫВАНИЯ НАЖМИТЕ CTRL+C\n\n')
  try:
    for q_user in m_data:
      print(f'Авторизация пользователя {q_user["login"]}')
      q_api = vk.DirectUserAPI(user_login=q_user['login'], user_password=q_user['pass'], scope='messages',v='5.131')
      q_groups = q_api.groups.get()['items']
      print(f'У пользователя найдено {len(q_groups)} групп')
      #print(q_groups)
      for q_wall in q_groups:
        print(f'Отправка поста в группу {q_wall}')
        q_api.wall.post(owner_id="-"+str(q_wall),message=f_msg,attachment=f_photo)
        print('отправлено!')
        time.sleep(f_pause)
  except Exception as e:
    print('Рассылка прервана: ОШИБКА')
    print(e)


def cycle():
  print(f'''Менеджер рассылки ВК
Сохранено {len(m_data)} акаунтов
Вводите команды латинскими буквами для управления:
a - для добавления акаунта
l - что бы увидеть список акаунтов
s - что бы начать рассылку''')
  f_key = input('>>')
  if f_key == 'a':
    add_acc()
  elif f_key == 'l':
    list_acc()
  elif f_key == 's':
    start_spam()
  cycle()

def init():
  global m_data
  f_data = get_data()
  if f_data != 0:
    m_data = f_data['users']
  cycle()

if __name__ == "__main__":
    init()