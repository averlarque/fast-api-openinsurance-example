from __future__ import annotations

from typing import List, Optional

from fastapi import FastAPI, Query
from pydantic import conint

from models import Claim, Driver, MotorCoverage, Vehicle
import json
from pathlib import Path

app = FastAPI(
    title='Open Insurance (OPIN) API',
    description='Open API specification developed for OPIN by Bhagvan Kommadi',
    contact={'email': 'connect@openinsurance.io'},
    license={
        'name': 'Apache 2.0',
        'url': 'http://www.apache.org/licenses/LICENSE-2.0.html',
    },
    version='1.0.1'
)

current_directory = Path(__file__).parent

@app.get('/claim', response_model=List[Claim], tags=['developers'])
def search_claim_by_claim_id(
    search_string: Optional[str] = Query(None, alias='searchString'),
    skip: Optional[conint(ge=0)] = None,
    limit: Optional[conint(ge=0, le=50)] = None,
) -> List[Claim]:
    """
    returns claim
    """
    pass


@app.post('/claim', response_model=None, tags=['admins'])
def add_claim(body: Claim = None) -> None:
    """
    adds a claim
    """
    pass


@app.get('/driver', response_model=List[Driver], tags=['developers'])
def search_driver_by_driver_id(
    search_string: Optional[str] = Query(None, alias='searchString'),
    skip: Optional[conint(ge=0)] = None,
    limit: Optional[conint(ge=0, le=50)] = None,
) -> List[Driver]:
    """
    returns driver
    """
    pass


@app.post('/driver', response_model=None, tags=['admins'])
def add_driver(body: Driver = None) -> None:
    """
    adds a Driver
    """
    pass


@app.get('/motorCoverage', response_model=List[Driver], tags=['developers'])
def search_motor_coverage_by_motor_coverage_id(
    search_string: Optional[str] = Query(None, alias='searchString'),
    skip: Optional[conint(ge=0)] = None,
    limit: Optional[conint(ge=0, le=50)] = None,
) -> List[Driver]:
    """
    returns motorCoverage
    """
    pass


@app.post('/motorCoverage', response_model=None, tags=['admins'])
def add_motor_coverage(body: MotorCoverage = None) -> None:
    """
    adds a MotorCoverage
    """
    pass


@app.get('/vehicle', response_model=List[Vehicle], tags=['developers'])
def search_vehicle_by_vehicle_id(
    search_string: Optional[str] = Query(None, alias='searchString'),
    skip: Optional[conint(ge=0)] = None,
    limit: Optional[conint(ge=0, le=50)] = None,
) -> List[Vehicle]:
    """
    returns vehicle
    """
    file_path = current_directory / 'examples' / 'vehicles.json'
    with open(file_path, 'r') as file:
        parsed_data = json.load(file)

    result = [Vehicle(**item_data) for item_data in parsed_data]
    return result


@app.post('/vehicle', response_model=None, tags=['admins'])
def add_vehicle(body: Vehicle = None) -> None:
    """
    adds a vehicle
    """
    pass
