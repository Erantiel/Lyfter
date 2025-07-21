import Controller as con

def test_add_financial_flow_type_parameter_empty_returns_type_error():
    # Arrange
    empty_type = ''
    # Act
    result = con.add_financial_flow('','Category','Description','2')
    # Assert
    assert result == TypeError


def test_add_financial_flow_category_parameter_empty_returns_type_error():
    # Arrange
    empty_category = ''
    # Act
    result = con.add_financial_flow('Type',empty_category,'Description','2')
    # Assert
    assert result == TypeError


def test_add_financial_flow_description_parameter_empty_returns_type_error():
    # Arrange
    empty_description = ''
    # Act
    result = con.add_financial_flow('Type','Category',empty_description,'2')
    # Assert
    assert result == TypeError


def test_add_financial_flow_amount_parameter_string_returns_value_error():
    # Arrange
    letter_amount = 'A'
    # Act
    result = con.add_financial_flow('Type','Category','Description', letter_amount)
    # Assert
    assert result == ValueError


def test_add_financial_flow_all_patameter_correct_returns_proper_object_properties():
    # Arrange
    # Act
    result = con.add_financial_flow('Type','Category','Description','10')
    # Assert
    assert f'{result.type},{result.category},{result.description},{result.amount}' == 'Type,Category,Description,10.0'


def test_add_financial_flow_amount_parameter_string_number_returns_correct_value_as_float_or_integer():
    # Arrange
    string_number_amount = '2'
    # Act
    result = con.add_financial_flow('Type','Category','Description', string_number_amount)
    # Assert
    assert result.amount == 2


def test_open_financial_flow_file_missing_file_return_missing_file_not_found_error():
    # Arrange
    # Act
    result = con.open_financial_flow_file()
    # Assert
    assert result == FileNotFoundError


def test_open_category_file_missing_file_return_missing_file_not_found_error():
    # Arrange
    # Act
    result = con.open_category_file()
    # Assert
    assert result == FileNotFoundError