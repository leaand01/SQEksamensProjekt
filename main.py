from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from MVC.Models_DTO.DropDownBankNamesController import dropdown_bank_names
from MVC.Models_DTO.PrincipalController import principal

app = FastAPI()
views = Jinja2Templates(directory='MVC/Views')


@app.get('/')
def welcome_page(request: Request):
    return views.TemplateResponse('index.html', {'request': request, 'dropdown_bank_names': dropdown_bank_names})


@app.post('/', response_class=HTMLResponse)
async def welcome_page_with_calc_result(request: Request):
    user_inputs = await request.form()
    user_inputs = user_inputs._dict
    principal.calculate(user_inputs)
    return views.TemplateResponse('index_pressed_submit.html',
                                  {'request': request,
                                   "dropdown_bank_names": dropdown_bank_names,
                                   'input_house_price': principal.user_inputs['house_price'],
                                   'input_down_payment': principal.user_inputs['down_payment'],
                                   'input_bond_price': principal.user_inputs['bond_price'],
                                   'selected_bank': principal.user_inputs['dropdown'],
                                   "principal_value": principal.principal,
                                   "capital_loss": principal.capital_loss
                                   })

# Remark: According to .net MVC setup this corresponds to a Controller, since handles html requests.
