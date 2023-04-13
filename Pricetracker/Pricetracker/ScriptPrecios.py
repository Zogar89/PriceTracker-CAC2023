import requests

def get_item_info(item_id, proxies=None):
    url = f'https://api.mercadolibre.com/items/{item_id}'
    response = requests.get(url, proxies=proxies, verify=False) # Agregar verify=False

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

def main():
    item_id = "MLA885707733"
    # Reemplaza 'http://proxy.example.com:8080' con la URL de tu proxy
    proxy_url = 'http://proxy01:80'
    proxies = {
        'http': proxy_url,
        'https': proxy_url,
    }

    item_info = get_item_info(item_id, proxies)

    if item_info is not None:
        print(f"ID del artículo: {item_info['id']}")
        print(f"Titulo: {item_info['title']}")
        print("Precios:")

        # Imprimir el precio regular del artículo
        print(f"  - Precio regular: {item_info['price']} {item_info['currency_id']}")

        # Imprimir todos los precios adicionales
        if 'prices' in item_info and 'prices' in item_info['prices']:
            for price in item_info['prices']['prices']:
                price_type = price['type']
                amount = price['amount']
                currency_id = price['currency_id']

                if 'presentation' in price and 'display_conditions' in price['presentation']:
                    conditions = price['presentation']['display_conditions']
                    level_id = conditions['buyer_level_id']
                    print(f"  - {price_type} (Nivel del comprador {level_id}): {amount} {currency_id}")
                else:
                    print(f"  - {price_type}: {amount} {currency_id}")
        else:
            print("No hay precios adicionales disponibles.")
    else:
        print("No se pudo obtener información del artículo.")

if __name__ == '__main__':
    main()