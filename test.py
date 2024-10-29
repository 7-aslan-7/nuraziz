import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode

API_TOKEN = '6560882506:AAHoHoIZobShtd2vL_G4ebotigiqrnslhWc'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Пример данных
schedule = {
    "1А": ["🧮 Математика - 08:00", "📖 Русский язык - 09:00", "📜 История - 10:00"],
    "1Б": ["🔬 Физика - 08:00", "🧮 Математика - 09:00", "🌍 География - 10:00"]
}
events = ["🎉 Школьный концерт - *15 ноября*", "🏅 Олимпиада по математике - *25 ноября*"]
contacts = {
    "👩‍🏫 Учитель математики": "@math_teacher",
    "👨‍🏫 Классный руководитель": "@class_teacher"
}
news = ["🍂 *Осенние каникулы* с *28 октября*", "📅 Новое расписание с *1 ноября*"]

# Команда /start с красивым оформлением
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("📅 Расписание занятий", callback_data="schedule"),
        InlineKeyboardButton("🎈 События школы", callback_data="events"),
        InlineKeyboardButton("📞 Контакты учителей", callback_data="contacts"),
        InlineKeyboardButton("📰 Новости и объявления ", callback_data="news")
    )

    welcome_text = (
        "👋 *Привет!* Я ваш школьный бот-помощник.\n\n"
        "📌 С помощью меня ты можешь:\n"
        "• Узнать расписание занятий\n"
        "• Отыскать контакты учителей\n"
        "• Быть в курсе школьных событий и новостей\n\n"
        "Выбери нужный раздел ниже:"
    )
    await message.answer(welcome_text, reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)

# Расписание занятий
@dp.callback_query_handler(lambda c: c.data == "schedule")
async def show_schedule(callback_query: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup()
    for class_name in schedule:
        keyboard.add(InlineKeyboardButton(f"📚 {class_name}", callback_data=f"class_{class_name}"))
    await callback_query.message.answer("📅 *Выберите класс для просмотра расписания:*", reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)

@dp.callback_query_handler(lambda c: c.data.startswith("class_"))
async def display_class_schedule(callback_query: types.CallbackQuery):
    class_name = callback_query.data.split("_")[1]
    class_schedule = "\n".join(schedule.get(class_name, []))
    await callback_query.message.answer(f"📚 *Расписание для класса {class_name}:*\n\n{class_schedule}", parse_mode=ParseMode.MARKDOWN)

# События школы
@dp.callback_query_handler(lambda c: c.data == "events")
async def show_events(callback_query: types.CallbackQuery):
    events_text = "\n".join(events)
    await callback_query.message.answer(f"🎉 *Ближайшие школьные события:*\n\n{events_text}", parse_mode=ParseMode.MARKDOWN)

# Контакты учителей и администрации
@dp.callback_query_handler(lambda c: c.data == "contacts")
async def show_contacts(callback_query: types.CallbackQuery):
    contacts_text = "\n".join([f"{role}: {contact}" for role, contact in contacts.items()])
    await callback_query.message.answer(f"📞 *Контакты учителей:*\n\n{contacts_text}", parse_mode=ParseMode.MARKDOWN)

# Новости и объявления
@dp.callback_query_handler(lambda c: c.data == "news")
async def show_news(callback_query: types.CallbackQuery):
    news_text = "\n".join(news)
    await callback_query.message.answer(f"📰 *Последние новости и объявления:*\n\n{news_text}", parse_mode=ParseMode.MARKDOWN)

    
    
executor.start_polling(dp, skip_updates=True)
