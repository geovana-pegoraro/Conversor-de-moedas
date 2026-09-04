import urllib.request
import json

def converter_moeda(de="USD", para="BRL", valor=1.0):
    url = f"https://open.er-api.com/v6/latest/{de.upper()}"
    
    try:
        req = urllib.request.urlopen(url)
        dados = json.loads(req.read().decode())
        
        if dados.get("result") == "success":
            taxa = dados["rates"].get(para.upper())
            if taxa:
                resultado = valor * taxa
                print(f"{valor} {de.upper()} = {resultado:.2f} {para.upper()}")
            else:
                print(f"Moeda de destino '{para}' não encontrada.")
        else:
            print("Erro ao obter dados de câmbio.")
            
    except Exception as e:
        print(f"Erro na requisição: {e}")

if __name__ == "__main__":
    print("=== Conversor de Moedas Simple ===")
    converter_moeda("USD", "BRL", 50)
