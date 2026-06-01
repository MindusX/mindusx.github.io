def test_send_sms(client, app):
    # create user
    u = User(email='test@example.com')
    u.set_password('secret')
    db.session.add(u)
    db.session.commit()

    # login
    client.post('/login', data={'email': 'test@example.com', 'password': 'secret'})

    # send
    resp = client.post('/send', data={
        'to_number': '+33123456789',
        'message': 'Hello'
    })
    assert resp.status_code == 302  # redirect