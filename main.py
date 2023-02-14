from aiogram import *
import CuteON

API_TOKEN = CuteON.Get_.getLine("Config.sws", "token")


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)




@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("strt success!")


@dp.message_handler(commands=['add'])
async def insert(msg: types.Message):
    massage = msg.text
    content = massage.split()

    comm = content[0]
    teg = content[1]
    class_ = content[2]
    txt = content[3]

    file = open("Users/Buff", "a")
    file.write('<'+ teg +' class="' + class_ + '">\n' + txt + '\n</'+ teg +'>')

@dp.message_handler(commands=['td'])
async def insert(msg: types.Message):
    massage = msg.text
    content = massage.split()

    comm = content[0]
    num = content[1]
    txt = content[2]

    
    list_ = txt.split(",")
    day = []
    day.append(num)
    for i in list_:
        print(i)
        
        if i == 'инф':
            day.append( 'Информатика')

        if i == "мат":
            day.append( 'Математика')

        if i == "рус":
            day.append( 'Русский')

        if i == "лит":
            day.append( 'Литература')

        if i == "рум":
            day.append( 'Румынский')

        if i == "хим":
            day.append( 'Химия')

        if i == "ист":
            day.append( 'История')

        if i == "физ":
            day.append( 'Физика')

        if i == "био":
            day.append( 'Биология')

        if i == "гео":
            day.append( 'География')

        if i == "фра":
            day.append( 'Француский')

        if i == "фир":
            day.append( 'Физкультура')

        if i == "раз":
            day.append( 'Развитие личьности')

        if i == "гра":
            day.append( 'гражданское воспитание')



        
    fin_day = []
    for q in day:
        fin_day.append('<td>'+str(q)+"</td>")
    
    fin = " ".join(fin_day)

    file = open("Users/Buff", "a")
    file.write("<tr>\n" + fin + '\n</tr>')

    await msg.reply(fin)





@dp.message_handler(commands=['ping'])
async def send_welcome(msg: types.Message):
    await msg.reply("ваш id = " + str(msg.from_user.id))

@dp.message_handler(commands=['cls'])
async def send_welcome(msg: types.Message):
    file = open("Users/"+str(msg.from_user.id)+".html", "w")
    file.write(" ")
    file = open("Users/Buff", "w")
    file.write(" ")
    await msg.reply("Очищено")

@dp.message_handler(commands=['reg'])
async def send_welcome(msg: types.Message):
    CuteON.Write_.WriteStr("Users/users.sws", "public::"+ str(msg.from_user.id)+ "::" + str(msg.from_user.id))
    await msg.reply("Добавлено как: " + str(msg.from_user.id))

@dp.message_handler(commands=['div'])
async def send_welcome(msg: types.Message):
    massage = msg.text
    content = massage.split()

    comm = content[0]
    num = content[1]
    style = content[2]
    txt = content[3]
    day = []
    if num == "1":
        day.append('<div class="day">Понидельник</div>')
    if num == "2":
        day.append('<div class="day">Вторник</div>')
    if num == "3":
        day.append('<div class="day">Среда</div>')
    if num == "4":
        day.append('<div class="day">Четверг</div>')
    if num == "5":
        day.append('<div class="day">Пятница</div>')

    for i in txt.split(','):
        if i == 'инф':
            day.append( 'Информатика')

        if i == "мат":
            day.append( 'Математика')

        if i == "рус":
            day.append( 'Русский')

        if i == "лит":
            day.append( 'Литература')

        if i == "рум":
            day.append( 'Румынский')

        if i == "хим":
            day.append( 'Химия')

        if i == "ист":
            day.append( 'История')

        if i == "физ":
            day.append( 'Физика')

        if i == "био":
            day.append( 'Биология')

        if i == "гео":
            day.append( 'География')

        if i == "фра":
            day.append( 'Француский')

        if i == "фир":
            day.append( 'Физкультура')

        if i == "раз":
            day.append( 'Развитие личьности')

        if i == "гра":
            day.append( 'гражданское воспитание')

    fin_day = []
    for q in day:
        fin_day.append('<ul>'+str(q)+"</ul>")
    
    fin = " ".join(fin_day)

    file = open("Users/Buff", "a")
    file.write('<div class="block">\n' + fin + '\n</div>')

@dp.message_handler(commands=['finish'])
async def send_welcome(msg: types.Message):
    massage = msg.text
    content = massage.split()

    comm = content[0]
    style = content[1]
    mod = content[2]

    f = open("Styles/"+style+".html", "r")
    t = f.read()
    t_split =t.split("<cut>")

    file = open("Users/Buff", "r")
    text = file.read()

    UserNmae = str(msg.from_user.id)


    if mod == "table":
        with open("Users/"+UserNmae+".html", 'w') as file:
            file.write((t_split[0] + '<tr><td class="nameCol" >Номер урока</td> <td class="nameCol">Понидельник</td> <td class="nameCol">Вторник</td> <td class="nameCol">Среда</td> <td class="nameCol">Четверг</td> <td class="nameCol">Пятница</td></tr>' + text + t_split[1]).encode().decode())

    if mod == "md":
        with open("Users/"+UserNmae+".html", 'w') as file:
            file.write((t_split[0] + text + t_split[1]).encode().decode())

    await msg.reply("`Зборка завершина`")
    await msg.reply_document(open("Users/"+UserNmae+".html", 'rb'))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)