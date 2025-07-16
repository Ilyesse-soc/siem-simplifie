# Instructions Grafana

1. Lance Grafana (tu peux l’ajouter dans Docker si besoin)
2. Va sur http://localhost:3000
3. Login: admin / admin
4. Ajoute une nouvelle source de données :
   - Type : Elasticsearch
   - URL : http://localhost:9200
   - Index name : siem-logs
5. Crée ton dashboard avec les logs
