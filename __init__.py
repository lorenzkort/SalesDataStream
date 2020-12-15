import datetime
import logging
import azure.functions as func

from scrapers.careerguide import check_careerguide
from scrapers.monsterboard import check_monsterboard


def main():#main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    '''
    if mytimer.past_due:
        logging.info('The timer is past due!')
    '''
    logging.info('Python timer trigger function ran at %s', utc_timestamp)

    # datakwaliteit
    kws = ['Data Stewardship', 'Data Steward', 'Datakwaliteit']
    for kw in kws:
        check_monsterboard(kw, chat_id='-459671235')
        check_careerguide(kw, chat_id='-459671235')

    # customer due diligence
    kws = ['CDD' , 'KYC', 'Transactiemonitoring']
    for kw in kws:
        check_monsterboard(kw, chat_id='-487901102')
        check_careerguide(kw, chat_id='-487901102')
    return

if __name__ == "__main__":
    main()