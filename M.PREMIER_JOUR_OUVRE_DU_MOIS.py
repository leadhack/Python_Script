import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.exceptions import AirflowSkipException
import holidays
from pytz import timezone
local_tz = timezone('Europe/Paris')
# Définir les jours fériés pour votre pays (ici, la France)
country_holidays = holidays.France()
def check_premier_jour_ouvre(**kwargs):
    today = pendulum.now().date()
    if today.weekday() >= 5:  # 5 = samedi, 6 = dimanche
        raise AirflowSkipException("DAG ignoré car c'est un week-end.")
    elif today in country_holidays:
        raise AirflowSkipException("DAG ignoré car c'est un jour férié.")
    first_day = today.replace(day=1) # je remplace aujourd'hui par 1 afin que je parcour les jour pour trouver le 1er jour ouvré
    while first_day.weekday() >= 5 or first_day in country_holidays:
        first_day = first_day.add(days=1) # passer au jour qui suit jusqu'à je trouve le premier jour ouvré
    if today != first_day: #Si first_day recupéré egal par exemple le 2/10 et today = 12/10 alors je suis pas dans le premier jour ouvré
        raise AirflowSkipException("DAG ignoré car ce n'est pas le premier jour ouvré du mois.")
    else:
        print("C'est le premier jour ouvré du mois. Le traitement peut continuer.")
def task_to_run():
    print("Exécution de la tâche car c'est le premier Jeudi du mois")
default_args = {
    'owner': 'Mehdi',
    'start_date': pendulum.datetime(2024, 8, 3, tz=local_tz),}
# Définir le DAG
with DAG(
    "M.PREMIER_JOUR_OUVRE_DU_MOIS",
    default_args=default_args,
    schedule_interval="0 0 1 * *",  # S'exécute le 1er jour de chaque mois
    catchup=False
) as dag:
    check_if_premier_jour_ouvre = PythonOperator(
        task_id="check_premier_jour_ouvre",
        python_callable=check_premier_jour_ouvre)
    run_task = PythonOperator(
        task_id='run_task',
        python_callable=task_to_run)
# Le DAG s'exécutera seulement si c'est le premier jour ouvré du mois
check_if_premier_jour_ouvre >> run_task
