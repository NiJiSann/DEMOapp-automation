from midterm_project import keys

address_data_1 = {
    keys.full_name: '',
    keys.address1: '',
    keys.city: '',
    keys.zip_code: '',
    keys.country: ''
}

address_data_2_correct = {
    keys.full_name: 'Bill',
    keys.address1: 'Shibuya',
    keys.city: 'Tokyo',
    keys.zip_code: '100',
    keys.country: 'Japan'
}

card_data_1 = {
    keys.card_name: '',
    keys.card_num: '',
    keys.exp_date: '',
    keys.security_code: ''
}

card_data_2 = {
    keys.card_name: '',
    keys.card_num: '',
    keys.exp_date: 'qwert',
    keys.security_code: '111'
}

card_data_3 = {
    keys.card_name: '',
    keys.card_num: '',
    keys.exp_date: '1111',
    keys.security_code: '111'
}

card_data_4 = {
    keys.card_name: '',
    keys.card_num: '',
    keys.exp_date: '1133',
    keys.security_code: 'qwert'
}

card_data_5 = {
    keys.card_name: '',
    keys.card_num: '',
    keys.exp_date: '1133',
    keys.security_code: '1111'
}

card_data_6 = {
    keys.card_name: '',
    keys.card_num: '',
    keys.exp_date: '1124',
    keys.security_code: '111'
}

card_data_7_correct = {
    keys.card_name: 'Bill',
    keys.card_num: '5555555555554444',
    keys.exp_date: '1124',
    keys.security_code: '111'
}

data_to_check = {
    keys.card_name: 'Bill',
    keys.card_num: '5555 5555 5555 4444',
    keys.exp_date: '11/24',
    keys.security_code: '111',
    keys.full_name: 'Bill',
    keys.address1: 'Shibuya',
    keys.city: 'Tokyo',
    keys.zip_code: '100',
    keys.country: 'Japan'
}