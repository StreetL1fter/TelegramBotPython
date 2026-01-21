from aiogram import F,Router,types,Bot
from aiogram.filters import Command
from aiogram.types import LoginUrl
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import FSInputFile
from aiogram.enums import ParseMode
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from pathlib import Path

from app.database.database import save_user


router = Router()


class UserState(StatesGroup):
    name = State()
    email = State()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.button(text="Пауэрлифтинг 🏋️‍♂️",callback_data="powerlifting")
    builder.button(text="Бодибилдинг 🦾",callback_data="bodybuilding")
    builder.button(text="Авторы 📖",callback_data="author")
    builder.button(text="Жимовые раскладки 📕", callback_data="bench_press")
    builder.button(text="Гайды 📚",callback_data="gaids")
    builder.button(text="Купить персональное введение", callback_data = 'personal_trener')
    builder.adjust(2,1)
    await message.answer(f"Привет! {message.from_user.first_name} Я тренировочный бот,\tБот в котором вы можете получить тренировку для себя и не платить ни копейки! 🚀",reply_markup=builder.as_markup())
    

def powerlifting_menu():
    builder1 = InlineKeyboardBuilder()
    builder1.button(text="Высокий", callback_data="highlevel")
    builder1.button(text="Лёгкий",callback_data="lowlevel")
    builder1.button(text="Назад ◀️", callback_data="back_to_main")
    builder1.adjust(2)
    return builder1.as_markup()

def Genderbodybuilding_menu():
    builder1 = InlineKeyboardBuilder()
    builder1.button(text="Мужчина 🤵‍♂️", callback_data="manlevel")
    builder1.button(text="Женщина 👩‍🦰",callback_data="womanlevel")
    builder1.button(text="Назад ◀️", callback_data="back_to_main")
    builder1.adjust(2)
    return builder1.as_markup()

def bodybuilding_menu():
        builder1 = InlineKeyboardBuilder()
        builder1.button(text="Больше 3-4 лет", callback_data="highlevelbody")
        builder1.button(text="Меньше трёх лет",callback_data="lowlevelbody")
        builder1.button(text="Назад ◀️", callback_data="back_to_main")
        builder1.adjust(2)
        return builder1.as_markup()

def womanbodybuilding_menu():
    builder1 = InlineKeyboardBuilder()
    builder1.button(text="Больше 3-4 лет", callback_data="womanhighlevelbody")
    builder1.button(text="Меньше трёх лет",callback_data="womanlowlevelbody")
    builder1.button(text="Назад ◀️", callback_data="back_to_main")
    builder1.adjust(2)
    return builder1.as_markup()


def author_menu():
    buildermenu = InlineKeyboardBuilder()
    buildermenu.button(text="Telegram", url="https://t.me/ne1romediator")
    buildermenu.button(text="VK", url="https://vk.com/is_ma5")
    buildermenu.button(text="Назад ◀️", callback_data="back_to_main")
    buildermenu.adjust(3)
    return buildermenu.as_markup()

def gaids():
    buildergaids = InlineKeyboardBuilder()
    buildergaids.button(text="📕 Гайд - набор мышечной массы",url="https://telegra.ph/Rekompoziciya-sushka-12-09")
    buildergaids.button(text="📗 Гайд - профицит, дефицит каллорий(набор, сушка)",url="https://telegra.ph/Hh-06-01-10")
    buildergaids.button(text="📘 Гайд - увеличение силовых показателей",url="https://telegra.ph/Progress---ehto-ne-skuchno-s-07-09")
    buildergaids.button(text="📙 Гайд - как уберечься от травм",url="https://telegra.ph/Testovyj-dokument-07-09")
    buildergaids.adjust(1)
    return buildergaids.as_markup()

@router.callback_query(F.data=="highlevel")
async def highlevelgeneral(callback:types.CallbackQuery):
    current_dir = Path(__file__).parent
    file_path = current_dir / ".." / ".." / "data" / "training_cycles" / "Линейный цикл для продвинутых.xlsx"
    document = FSInputFile(str(file_path))
    builder3 = InlineKeyboardBuilder()
    builder3.button(text="Назад ◀️", callback_data="back_to_main")
    await callback.message.answer_document(document,caption="Уровень Высокий 🔴 - Пауэрлифтинг",reply_markup=builder3.as_markup())
    try:
        await callback.message.delete()
    except:
        pass

@router.callback_query(F.data=="lowlevel")
async def highlevelgeneral(callback:types.CallbackQuery):
    current_low = Path(__file__).parent
    file_path_low = current_low / ".." / ".." / "data" / "training_cycles" /"Цикл начального уровня.xlsx"
    document = FSInputFile(str(file_path_low))
    builder3 = InlineKeyboardBuilder()
    builder3.button(text="Назад ◀️", callback_data="back_to_main")
    await callback.message.answer_document(document,caption="Уровень Низкий 🟢 - Пауэрлифтинг",reply_markup=builder3.as_markup())
    try:
        await callback.message.delete()
    except:
        pass

@router.callback_query(F.data=="manlevel")
async def manlevel(callback:types.CallbackQuery):
    await callback.message.edit_text(
        "Выберите уровень стажа:",
        reply_markup=bodybuilding_menu()
    )
    await callback.answer()

@router.callback_query(F.data=="womanlevel")
async def manlevel(callback:types.CallbackQuery):
    await callback.message.edit_text(
        "Выберите уровень стажа:",
        reply_markup=womanbodybuilding_menu()
    )
    await callback.answer()


@router.callback_query(F.data == "powerlifting")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(
        
        "⚠️ Обращаем внимание - программы начального и среднего уровней подходят и мужчинам и женщинам,\n" \
        " так же внутри файла каждой программы есть инструкция с уточнениями или ответами на возможно возникшие вопросы.\n" \
        "\nВыберите уровень стажа:",
        reply_markup=powerlifting_menu()
    )
    try:
        await callback.message.delete()
    except:
        pass
    await callback.answer()

@router.callback_query(F.data == "bodybuilding")
async def send_random_value(callback: types.CallbackQuery):
    hidden_link = 'https://telegra.ph/Instrukciya-k-programmam-bb-11-01'
    answerquestion = ("<b>🦾Бодибилдинг</b> перед выбором пола, ознакомься со <a href='{}'>статьей</a>\t").format(hidden_link)
    await callback.message.answer(
        answerquestion,reply_markup=Genderbodybuilding_menu(),parse_mode="HTML")
    try:
        await callback.message.delete()
    except:
        pass
    await callback.answer()


@router.callback_query(F.data == "back_to_main")
async def backtomain(callback:types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.button(text="Пауэрлифтинг 🏋️‍♂️", callback_data="powerlifting")
    builder.button(text="Бодибилдинг 🦾",callback_data="bodybuilding")
    builder.button(text="Авторы 📖",callback_data="author")
    builder.button(text="Жимовые раскладки 📕", callback_data="bench_press")
    builder.button(text="Гайды 📚",callback_data="gaids")
    builder.button(text="Купить персональное введение", callback_data = 'personal_trener')
    builder.adjust(2,1)
    await callback.message.answer(
            f"Привет! Я тренировочный бот на aiogram 3.x!. Бот в котором вы можете получить тренировку для себя и не платить ни копейки! 🚀",
            reply_markup=builder.as_markup()
        )
    try:
        await callback.message.delete()
    except:
        pass
    
    await callback.answer()

@router.callback_query(F.data == "gaids")
async def gaids12(callback:types.CallbackQuery):
    current_bench = Path(__file__).parent
    file_path = current_bench / ".." / ".." / "data" / "training_cycles" / "zias-bench.gif"
    gaidsimage = FSInputFile(str(file_path))
    await callback.message.answer_photo(gaidsimage,caption="В данном разделе вы можете найти гайды по питанию/тренировкам и другие.",reply_markup=gaids())


@router.callback_query(F.data == "author")
async def author(callback:types.CallbackQuery):
    current_photoimage = Path(__file__).parent
    file_image = current_photoimage / ".." / ".." / "data" / "training_cycles" / "photoimageismail.jpg"
    photoimage = FSInputFile(str(file_image))
    await callback.message.answer_photo(photoimage,caption="<strong>Исмаил Мендгалиев</strong> - FullStack-Developer\n" \
    "\n✍️<b>Ниже представлены Соц-сети</b> автора данного телеграм бота, с которыми вы "
    "можете ознакомиться",parse_mode="HTML",reply_markup=author_menu())
    try:
        await callback.message.delete()
    except:
        pass
    await callback.answer()
        

@router.callback_query(F.data == "highlevelbody")
async def highlevelbody(callback:types.CallbackQuery):
    current_man = Path(__file__).parent
    file_image = current_man  / ".." / ".." / "data" / "training_cycles" / "Муж высокий 3дневный.xlsx"
    document = FSInputFile(str(file_image))
    builder3 = InlineKeyboardBuilder()
    builder3.button(text="Назад ◀️", callback_data="back_to_main")
    await callback.message.answer_document(document,caption="Уровень Высокий 🔴 - Бодибилдинг",reply_markup=builder3.as_markup())
    try:
        await callback.message.delete()
    except:
        pass

@router.callback_query(F.data == "lowlevelbody")
async def highlevelbody(callback:types.CallbackQuery):
    current_man_low = Path(__file__).parent
    file_image = current_man_low  / ".." / ".." / "data" / "training_cycles" / "Мужской начальный 3х дневный.xlsx"
    document = FSInputFile(str(file_image))
    builder3 = InlineKeyboardBuilder()
    builder3.button(text="Назад ◀️", callback_data="back_to_main")
    await callback.message.answer_document(document,caption="Уровень Низкий 🟢 - Бодибилдинг",reply_markup=builder3.as_markup())
    try:
        await callback.message.delete()
    except:
        pass

@router.callback_query(F.data == "womanhighlevelbody")
async def highlevelbody(callback:types.CallbackQuery):
    current_man_low = Path(__file__).parent
    file_image = current_man_low  / ".." / ".." / "data" / "training_cycles" / "Жен средний 3дневный.xlsx"
    document = FSInputFile(str(file_image))
    builder3 = InlineKeyboardBuilder()
    builder3.button(text="Назад ◀️", callback_data="back_to_main")
    await callback.message.answer_document(document,caption="Уровень Высокий 🔴 - Бодибилдинг",reply_markup=builder3.as_markup())
    try:
        await callback.message.delete()
    except:
        pass

@router.callback_query(F.data == "womanlowlevelbody")
async def highlevelbody(callback:types.CallbackQuery):
    current_man_low = Path(__file__).parent
    file_image = current_man_low  / ".." / ".." / "data" / "training_cycles" / "Жен начальный 3дневный.xlsx"
    document = FSInputFile(str(file_image))
    builder3 = InlineKeyboardBuilder()
    builder3.button(text="Назад ◀️", callback_data="back_to_main")
    await callback.message.answer_document(document,caption="Уровень Низкий 🟢 - Бодибилдинг",reply_markup=builder3.as_markup())
    try:
        await callback.message.delete()
    except:
        pass




@router.callback_query(F.data == "bench_press")
async def bench(callback:types.CallbackQuery):
    current_man_low = Path(__file__).parent
    file_image = current_man_low  / ".." / ".." / "data" / "training_cycles" / "bench_presses_article.docx"
    docx = FSInputFile(str(file_image))
    builder32 = InlineKeyboardBuilder()
    builder32.button(text="Назад",callback_data="back_to_main")
    await callback.message.answer_document(document=docx,reply_markup=builder32.as_markup())
    try:
        await callback.message.delete()
    except:
        pass


@router.callback_query(F.data == "personal_trener")
async def personal(callback:types.CallbackQuery):
    builder3 = InlineKeyboardBuilder()
    builder3.button(text="Ввод данных для оплаты",callback_data='questionnaire_for_payment')
    builder3.button(text="Назад ◀️", callback_data="back_to_main")
    file_larry = Path(__file__).parent
    photo_larry = file_larry  / ".." / ".." / "data" / "training_cycles" / "larry.webp"
    gaidsimage = FSInputFile(str(photo_larry))
    await callback.message.answer_photo(gaidsimage,caption='Привет если ты хочешь стать на шаг ближе к мечте,тебе необходимо заполнить все данные для оплаты',reply_markup=builder3.as_markup())


@router.callback_query(F.data == 'questionnaire_for_payment')
async def questionnaire(callback:types.CallbackQuery,state: FSMContext):
    await state.set_state(UserState.name)
    await callback.message.answer("Введите ваше имя")
    
@router.message(UserState.name)
async def process_name(message: types.Message,state:FSMContext):
    await state.update_data(name=message.text.strip())
    await state.set_state(UserState.email)
    await message.answer("Введите ваш email")

@router.message(UserState.email)
async def email_enter(message: types.Message,state:FSMContext):
    email= message.text.strip()
    user_id = message.from_user.id
    if '@' not in email or '.' not in email:
        await message.answer("Некорректный ввод,введите заново")
        return
    elif "@" not in email:
        await message.answer("Некорректный ввод email")
        return
    elif "." not in email:
        await message.answer("Некорректный ввод email")
        return
    else:
        await state.update_data(email=email)
        data = await state.get_data()
        name = data['name']
        save_user(user_id, name, email)
        await message.answer(f"Спасибо вот ваши данные\t\t\n{name},\t \n{email}")



@router.message()
async def echo(message: types.Message):
    builder_info = ReplyKeyboardBuilder()
    builder_info.button(text='Нормально,ты как?')
    builder_info.button(text="Не могу сейчас ответить тебе")
    await message.answer("Как сам?",reply_markup=builder_info.as_markup())


@router.message(F.text == "Нормально,ты как?")
async def normal(message:types.Message):
    await message.answer("Хорошо,понял!")
