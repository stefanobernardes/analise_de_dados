from src.stages.contracts.mocks.extract_contract import extract_contract_mock
from src.stages.contracts.transform_contract import TransformContract
from .transform_raw_data import TransformRawData

def test_transform():
    Transform_raw_data = TransformRawData()
    Transformed_data_contract = Transform_raw_data.transform(extract_contract_mock)
    
    assert isinstance(Transformed_data_contract, TransformContract)
    
