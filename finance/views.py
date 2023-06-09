from rest_framework.decorators import api_view
from django.http import JsonResponse, response


import requests
from bs4 import BeautifulSoup

url = "https://www.moneycontrol.com"
most_active_bse_url = "https://www.moneycontrol.com/stocks/marketstats/bse-mostactive-stocks/all-companies-97/"
most_active_nse_url = "https://www.moneycontrol.com/stocks/marketstats/nse-mostactive-stocks/all-companies-99/"
commodities_url = "https://www.moneycontrol.com/commodity/"


def get_soup(url=url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def get_most_active(market="nse"):
    soup = get_soup(url)
    stock_data = []
    market_div_id = "in_maNSE" if market == "nse" else "id_maBSE"
    div = soup.find(id=market_div_id)
    if div:
        table = div.find("table")

        if table:
            rows = table.find_all('tr')

            for row in rows[1:]:
                columns = row.find_all('td')
                stock_name = columns[0].text.strip()
                stock_price = columns[1].text.strip()
                stock_change = columns[2].text.strip()
                stock_data.append({
                    'stock_name': stock_name,
                    'stock_price': stock_price,
                    'stock_change': stock_change
                })

    return stock_data


def get_market_action():
    soup = get_soup(url)
    market_action_data = []
    div = soup.find(id="market_action")
    table = div.find(class_="srl_MA")
    if table:
        rows = table.find_all('tr')
        for row in rows[1:]:
            columns = row.find_all('td')
            market_name = columns[0].text.strip()
            market_price = columns[1].text.strip()
            market_change = columns[2].text.strip()
            market_percentage_change = columns[3].text.strip()

            market_action_data.append({
                'market_name': market_name,
                'market_price': market_price,
                'market_change': market_change,
                'market_percentage_change': market_percentage_change
            })
        return market_action_data


def get_most_active_bse_stocks():
    soup = get_soup(most_active_bse_url)
    table = soup.find(class_="bsr_table hist_tbl_hm").find("table")
    bse_most_active_data = []

    if table:
        rows = table.find_all('tr')
        if (len(rows) > 10):
            for row in rows[1:]:
                columns = row.find_all('td')[:7]
                if (len(columns) < 7):
                    continue
                company_name = columns[0].text.split("\n")[0]
                group = columns[1].text.strip()
                high = columns[2].text.strip()
                low = columns[3].text.strip()
                last_price = columns[4].text.strip()
                percentage_change = columns[5].text.strip()
                value = columns[6].text.strip()

                bse_most_active_data.append({
                    'company_name': company_name,
                    'group': group,
                    'high': high,
                    'low': low,
                    'last_price': last_price,
                    'percentage_change': percentage_change,
                    'value': value
                })
        return bse_most_active_data


def get_most_active_nse_stocks():
    soup = get_soup(most_active_nse_url)
    table = soup.find(class_="bsr_table hist_tbl_hm").find("table")
    nse_most_active_data = []

    if table:
        rows = table.find_all('tr')
        if (len(rows) > 10):
            for row in rows[1:]:
                columns = row.find_all('td')[:7]
                if (len(columns) < 7):
                    continue
                company_name = columns[0].text.split("\n")[0]
                high = columns[1].text.strip()
                low = columns[2].text.strip()
                last_price = columns[3].text.strip()
                percentage_change = columns[4].text.strip()
                value = columns[5].text.strip()

                nse_most_active_data.append({
                    'company_name': company_name,
                    'high': high,
                    'low': low,
                    'last_price': last_price,
                    'percentage_change': percentage_change,
                    'value': value
                })
        return nse_most_active_data


def get_top_gainers(market="nifty"):
    soup = get_soup(url)
    top_gainers_data = []
    table = soup.find(id="in_tgNifty" if market ==
                      "nifty" else "in_tgSensex").find("table")

    if table:
        rows = table.find_all('tr')

        for row in rows[1:]:
            columns = row.find_all('td')
            company_name = columns[0].text.strip()
            price = columns[1].text.strip()
            change = columns[2].text.strip()
            percentage_change = columns[3].text.strip()

            top_gainers_data.append({
                'company_name': company_name,
                'price': price,
                'change': change,
                'percentage_change': percentage_change
            })
        return top_gainers_data


def get_top_losers(market="nifty"):
    soup = get_soup(url)
    top_losers_data = []
    table = soup.find(id="in_tlNifty" if market ==
                      "nifty" else "in_tlSensex").find("table")

    if table:
        rows = table.find_all('tr')

        for row in rows[1:]:
            columns = row.find_all('td')
            company_name = columns[0].text.strip()
            price = columns[1].text.strip()
            change = columns[2].text.strip()
            percentage_change = columns[3].text.strip()

            top_losers_data.append({
                'company_name': company_name,
                'price': price,
                'change': change,
                'percentage_change': percentage_change
            })
        return top_losers_data


def get_market_commodity_gainers(index="mcx"):
    soup = get_soup(commodities_url)
    market_commodity_gainers = {
        "mcx": [],
        "ncdex": []
    }
    ul = soup.find_all("ul", {"class": "market_stats_list"})
    if ul is not None:
        mcx_ul = ul[0]
        ncdex_ul = ul[1]
        mcx_list = mcx_ul.find_all("li")
        if (mcx_list):
            mcx_top_gainers_ele = mcx_list[0]
            mcx_top_gainers_table = mcx_top_gainers_ele.find("table")
            if mcx_top_gainers_table:
                rows = mcx_top_gainers_table.find_all('tr')

                for row in rows[1:]:
                    columns = row.find_all('td')
                    commodity_name = columns[0].text.strip()
                    price = columns[1].text.strip()
                    change = columns[2].text.strip()
                    percentage_change = columns[3].text.strip()

                    market_commodity_gainers["mcx"].append({
                        'commodity': commodity_name,
                        'price': price,
                        'change': change,
                        'percentage_change': percentage_change
                    })

        ncdex_list = ncdex_ul.find_all("li")
        if (ncdex_list):
            ncdex_top_gainers_ele = ncdex_list[0]
            ncdex_top_gainers_table = ncdex_top_gainers_ele.find("table")
            if ncdex_top_gainers_table:
                rows = ncdex_top_gainers_table.find_all('tr')

                for row in rows[1:]:
                    columns = row.find_all('td')
                    commodity_name = columns[0].text.strip()
                    price = columns[1].text.strip()
                    change = columns[2].text.strip()
                    percentage_change = columns[3].text.strip()

                    market_commodity_gainers["ncdex"].append({
                        'commodity': commodity_name,
                        'price': price,
                        'change': change,
                        'percentage_change': percentage_change
                    })

    return market_commodity_gainers


def get_market_commodity_losers():
    soup = get_soup(commodities_url)
    market_commodity_losers = {
        "mcx": [],
        "ncdex": []
    }
    ul = soup.find_all("ul", {"class": "market_stats_list"})
    if ul is not None:
        mcx_ul = ul[0]
        ncdex_ul = ul[1]
        mcx_list = mcx_ul.find_all("li")
        if (mcx_list):
            mcx_top_losers_ele = mcx_list[1]
            mcx_top_losers_table = mcx_top_losers_ele.find("table")
            if mcx_top_losers_table:
                rows = mcx_top_losers_table.find_all('tr')

                for row in rows[1:]:
                    columns = row.find_all('td')
                    commodity_name = columns[0].text.strip()
                    price = columns[1].text.strip()
                    change = columns[2].text.strip()
                    percentage_change = columns[3].text.strip()

                    market_commodity_losers["mcx"].append({
                        'commodity': commodity_name,
                        'price': price,
                        'change': change,
                        'percentage_change': percentage_change
                    })

        ncdex_list = ncdex_ul.find_all("li")
        if (ncdex_list):
            ncdex_top_losers_ele = ncdex_list[1]
            ncdex_top_losers_table = ncdex_top_losers_ele.find("table")
            if ncdex_top_losers_table:
                rows = ncdex_top_losers_table.find_all('tr')

                for row in rows[1:]:
                    columns = row.find_all('td')
                    commodity_name = columns[0].text.strip()
                    price = columns[1].text.strip()
                    change = columns[2].text.strip()
                    percentage_change = columns[3].text.strip()

                    market_commodity_losers["ncdex"].append({
                        'commodity': commodity_name,
                        'price': price,
                        'change': change,
                        'percentage_change': percentage_change
                    })

    return market_commodity_losers


@api_view(['GET'])
def mostActive(request):
    market = request.GET["market"]
    most_active = get_most_active(market=market)
    return JsonResponse({"data": most_active})


@api_view(['GET'])
def topGainers(request):
    market = request.GET["market"]
    top_gainers = get_top_gainers(market=market)
    return JsonResponse({"data": top_gainers, "table_config": {
        "headers": [
            "Name",
            "Price",
            "Change",
            "% Change"
        ],
        "keys": [
            "company_name",
            "price",
            "change",
            "percentage_change"
        ]
    }})


@api_view(['GET'])
def topLosers(request):
    market = request.GET["market"]
    top_losers = get_top_losers(market=market)
    return JsonResponse({"data": top_losers, "table_config": {
        "headers": [
            "Name",
            "Price",
            "Change",
            "% Change"
        ],
        "keys": [
            "company_name",
            "price",
            "change",
            "percentage_change"
        ]
    }})


@api_view(['GET'])
def marketAction(request):
    marketAction = get_market_action()
    return JsonResponse({"data": marketAction, "table_config": {
        "headers": [
            "Name",
            "Price",
            "Change",
            "% Change"
        ],
        "keys": [
            "market_name",
            "market_price",
            "market_change",
            "market_percentage_change"
        ]
    }})


@api_view(['GET'])
def marketCommodityGainers(request):
    commodities = get_market_commodity_gainers()
    return JsonResponse({"data": commodities, "table_config": {
        "headers": [
            "Name",
            "Price",
            "Change",
            "% Change"
        ],
        "keys": [
            "commodity",
            "price",
            "change",
            "percentage_change"
        ]
    }})


@api_view(['GET'])
def marketCommodityLosers(request):
    commodities = get_market_commodity_losers()
    return JsonResponse({"data": commodities, "table_config": {
        "headers": [
            "Name",
            "Price",
            "Change",
            "% Change"
        ],
        "keys": [
            "commodity",
            "price",
            "change",
            "percentage_change"
        ]
    }})
