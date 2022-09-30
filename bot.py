from telegram.ext import CommandHandler, MessageHandler, Filters, Updater
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from update import UpdateCsv, CidadesEs
import data
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("TOKEN")
admin_id = os.getenv("ADMIN_ID")
flag = ''
cidades = CidadesEs()
unique_city = list()
for i in cidades:
    unique_city.append([i.title()])


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Seja bem-vindo {}, estou aqui para lhe informar todos os dados a respeito do Corona Vírus no Espírito Santo".format(update.effective_user.first_name)
    )
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Digite /dados para encontrar informações da cidade desejada"
    )
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Digite /nome para escolher uma cidade"
    )
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Digite /mapa para visualizar o mapa de casos no estado"
    )


def receive(update, context):
    global flag

    if update.message.text.capitalize() in cidades:
        city = update.message.text.capitalize()
        bairros = data.top_neighborhood(city, info="active")
        str_b = str()

        i = 1
        for bairro in bairros:
            str_b += f"{i} - {bairro.title()}: {bairros[bairro]} Casos\n"
            i = i + 1
        update.message.reply_text(f"Dados sobre {city}:\n   -Casos Ativos: {data.active_cases(city)}\n  -CasosCasos Totais: {data.total_cases(city)} Casos")
        update.message.reply_text(f"Bairros com maior número de casos ativos: \n\n{str_b}")
        update.message.reply_text("Escolha uma opção:", reply_markup=ReplyKeyboardRemove(remove_keyboard=True))

    if update.message.text.lower() == "cep":
        update.message.reply_text("Digite seu CEP")
        flag = "cep"

    if flag == "cep":
        cep = update.message.text
        city = data.cep(cep)
        bairros = data.top_neighborhood(city, info="active")
        str_b = str()

        i = 1
        for bairro in bairros:
            str_b += f"{i} - {bairro.title()}: {bairros[bairro]} Casos\n"
            i = i + 1
        update.message.reply_text(
            f"Dados sobre {city}:\n -Casos Ativos: {data.active_cases(city)}\n  -Casos Totais: {data.total_cases(city)} Casos")
        update.message.reply_text(f"Bairros com maior número de casos ativos: \n\n{str_b}")
        flag = ''
        update.message.reply_text("Escolha uma opção:", reply_markup=ReplyKeyboardRemove(remove_keyboard=True))


def unknow(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Favor digitar um comando Válido"
    )


def city_name(update, context):
    global unique_city

    keyboard = unique_city

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)

    update.message.reply_text("Escolha uma opção:", reply_markup=reply_markup)


def updatedata(update, context):
    if update.effective_chat.id == admin_id:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Iniciando atualização dos Dados..."
        )

        UpdateCsv()
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Dados atualizados com sucesso!"
        )
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Você não possui permissão para executar esse comando"
        )


def city_option(update, context):
    keyboard = list()
    system_flag = "city_option"
    list_options = ["Nome da Cidade", "CEP", "Informações do Estado"]
    for i in list_options:
        opt = [i]
        keyboard.append(opt)

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)

    update.message.reply_text("Escolha uma opção:", reply_markup=reply_markup)


def map(update, context):
    update.message.reply_text("Processando mapa...")
    map_emote = u'\U0001F5FA'
    update.message.reply_text(f"Mapa Casos ativos Covid-19 Espírito Santo {map_emote}")
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('mapa.png', 'rb'))


def generate_map(update, context):
    if update.effective_chat.id == admin_id:
        data.generate_map()
        update.message.reply_text("Mapa gerado com sucesso!")
    else:
        update.message.reply_text("Apenas o administrador pode executar esse comando")


def main():
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), receive))

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('dados', city_option))
    dispatcher.add_handler(CommandHandler('nome', city_name))
    dispatcher.add_handler(CommandHandler('mapa', map))
    dispatcher.add_handler(CommandHandler('atualizar', updatedata))
    dispatcher.add_handler(CommandHandler('atmap', generate_map))

    dispatcher.add_handler(MessageHandler(Filters.command, unknow))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("Bot em Funcionamento, Precione CTRL + C para cancelar")
    main()
