from fastapi import FastAPI, Request
from scrapper import dotaBuffScrapping, heroes_list, \
                    counterBuffScrapper, titles, counterpicks
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get('/')
def get_home(request: Request):
    return templates.TemplateResponse("home_page/home.html",
                                      {"request": request})


@app.get('/info')
def get_hero_links(request: Request):
    return templates.TemplateResponse("heroes_page/heroes.html",
                                      {"request": request,
                                       "heroes": heroes_list()})


@app.get("/info/{item_id}")
def get_hero_info(request: Request, item_id: str):
    return templates.TemplateResponse("info_page/info.html",
                                      {"request": request,
                                       "hero_name": item_id,
                                       "titles": titles,
                                       "length": len(dotaBuffScrapping
                                                     (item_id)[0]),
                                       "statistics":
                                       dotaBuffScrapping(item_id)})


@app.get("/counter/{item_id}")
def get_hero_counters(request: Request, item_id: str):
    return templates.TemplateResponse("counter_page/counter.html",
                                      {"request": request,
                                       "hero_name": item_id,
                                       "counterpicks": counterpicks,
                                       "length": len(counterBuffScrapper
                                                     (item_id)[0]),
                                       "statistics":
                                       counterBuffScrapper(item_id)})
