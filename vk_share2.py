#v 0.1
import vk_api

import json
import time
import subprocess
import sys



# process output with an API in the subprocess module:
'''reqs = subprocess.check_output([sys.executable, '-m', 'pip',
'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
#print(installed_packages)
if "'vk'" not in installed_packages:
  print('vk is apsent, installing..')
  # implement pip as a subprocess:
  subprocess.check_call([sys.executable, '-m', 'pip', 'install',
  'vk'])'''
#import vk
'''s_login = '+79870848106'
s_pass ='@gC=cB,r)BK,G64'''
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
#result = vk.wall.post(owner_id="-"+str(f_groups['items'][0]),message="РџСЂРѕСЃС‚Рѕ С‚РµРєСЃС‚...!!!!!!!!!!!!!!!!!!!!!!!")
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


def captcha_handler(captcha):
  """ При возникновении капчи вызывается эта функция и ей передается объект
      капчи. Через метод get_url можно получить ссылку на изображение.
      Через метод try_again можно попытаться отправить запрос с кодом капчи
  """

  key = input("Enter captcha code {0}: ".format(captcha.get_url())).strip()
  print(key)
  # Пробуем снова отправить запрос с капчей
  return captcha.try_again(key)

def captcha_cathcer(captcha):
  try:
    key = input("Enter captcha code {0}: ".format(captcha.get_url())).strip()
    captcha.try_again(key)
  except vk_api.exceptions.Captcha as new_captcha:
    captcha_cathcer(new_captcha)

def add_acc():
  f_log = input('Введите логин\n>>')
  f_pass = input('Введите пароль\n>>')
  try:
    '''f_res = vk.DirectUserAPI(user_login=f_log,user_password=f_pass, scope='messages',v='5.131')
    f_res.auth_captcha_is_needed()
    f_res.'''
    vk_session = vk_api.VkApi(f_log, f_pass,captcha_handler=captcha_handler)
    vk_session.auth()

    #vk = vk_session.get_api()

    # print(vk.wall.post(message='Hello world!'))
    # f_groups = vk.groups.get()
    # print(f_groups)
    # result = vk.wall.post(owner_id="-"+str(f_groups['items'][0]),message="Просто текст...!!!!!!!!!!!!!!!!!!!!!!!")
  except Exception as e:
    print(e)
    add_acc()
    return

  #print(f_res)
  m_data.append({'login':f_log,'pass':f_pass})
  set_data({'users': m_data})
  print('Учетная запись добавлена')

def list_acc():
  for q in m_data:
    print(q['login'])

def start_spam():
  f_input = ''
  f_msg = ''
  while f_input != 'DONE':
    f_msg = f_msg + f_input+'\n'
    f_input = input('Напишите сообщение для рассылки\n>>')
  #f_msg = input('Напишите сообщение для рассылки\n>>')
  f_photo = input('Напишите адрес фото (вида photo124324_35345)\n>>')
  f_pause = int(input('Напишите паузу между постами, в секундах\n>>'))
  print('Рассылка запущена\n\nДЛЯ ПРЕРЫВАНИЯ НАЖМИТЕ CTRL+C\n\n')

  for q_user in m_data:
    try:
      print(f'Авторизация пользователя {q_user["login"]}')
      vk_session = vk_api.VkApi(q_user['login'], q_user['pass'], scope='messages,wall', captcha_handler=captcha_handler)
      vk_session.auth()

      vk = vk_session.get_api()


      f_groups = vk.groups.get()['items']
      print(f_groups)
      # result = vk.wall.post(owner_id="-"+str(f_groups['items'][0]),message="Просто текст...!!!!!!!!!!!!!!!!!!!!!!!")

      # q_api = vk.DirectUserAPI(user_login=q_user['login'], user_password=q_user['pass'], scope='messages',v='5.131')
      # q_groups = q_api.groups.get()['items']
      print(f'У пользователя найдено {len(f_groups)} групп')
      # print(q_groups)
      for q_wall in f_groups:
        try:
          
          print(f'Отправка поста в группу {q_wall}')
          # q_api.wall.post(owner_id="-"+str(q_wall),message=f_msg,attachment=f_photo)
          result = vk.wall.post(owner_id="-" + str(q_wall),
                                message=f_msg, attachment=f_photo)

          print('отправлено!')
        except Exception as e:
          print('Отправка не удалась: ОШИБКА')
          print(e)
        time.sleep(f_pause)
    except vk_api.exceptions.Captcha as captcha:
      captcha_cathcer(captcha)
    except Exception as e:
      print('Рассылка прервана: ОШИБКА')
      print(e)

def delete_acc():
  f_input = input('Напишите номер акка, который удалить\n>>')
  for q_acc in m_data:
    if q_acc['login'] == f_input:
      m_data.remove(q_acc)
      print(q_acc, ' удален из памяти')
      set_data({'users': m_data})
      return
  print('акаунт не найден')
  delete_acc()

def cycle():
  print(f'''Менеджер рассылки ВК
Сохранено {len(m_data)} акаунтов
Вводите команды латинскими буквами для управления:
a - для добавления акаунта
l - что бы увидеть список акаунтов
s - что бы начать рассылку
d - для удаления акаунат''')
  f_key = input('>>')
  if f_key == 'a':
    add_acc()
  elif f_key == 'l':
    list_acc()
  elif f_key == 's':
    start_spam()
  elif f_key == 'd':
    delete_acc()
  cycle()

def init():
  global m_data
  f_data = get_data()
  if f_data != 0:
    m_data = f_data['users']
  cycle()

if __name__ == "__main__":
    init()
