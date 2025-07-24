from ast import List
from sqlalchemy.orm import state
from sqlmodel import Session, select, true
from app.database.connection import engine
from app.models.beneficiarios import Beneficiario


def main():
    #obtener una sesión base de datos
    with Session(engine) as session:
        #ejecutar una query
        test_get_by_ccaf(session)

def test1(session: Session):
    print('Ejecutando test1')
    statement = select(Beneficiario)

    statement = statement.where(Beneficiario.ccaf == "La Araucana")
    statement = statement.limit(10)

    results = session.exec(statement).all()

    beneficiaries: list[Beneficiario] = []
    if results:
        for result in results:
            beneficiary = Beneficiario.model_validate(result, from_attributes=True)
            beneficiaries.append(beneficiary)

    print(beneficiaries[0])  


def test_get_by_ccaf(session: Session):
    print('Ejecutando test_get_by_ccaf')
    beneficiaries = Beneficiario.get_all_beneficiaries_by_ccaf(session, "La Araucana", 10)
    print(beneficiaries[0])

if __name__ == "__main__":
    main() 