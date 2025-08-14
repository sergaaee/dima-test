from pydantic import ConfigDict

user_get_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "email": "johndoe@example.com",
                "accounts": [
                    {"id": 1, "balance": 1000, "user_id": 1},
                    {"id": 2, "balance": 2500, "user_id": 1}
                ],
                "transactions": [
                    {
                        "id": 1,
                        "external_id": "txn_123",
                        "amount": 500,
                        "signature": "abc123",
                        "date": "2025-08-14T12:00:00",
                        "account_id": 1,
                        "user_id": 1
                    },
                    {
                        "id": 2,
                        "external_id": "txn_456",
                        "amount": 1500,
                        "signature": "def456",
                        "date": "2025-08-14T13:00:00",
                        "account_id": 2,
                        "user_id": 1
                    }
                ]
            }
        }
    )

user_login_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {"email": "johndoe", "password": "password123"}
        },
    )

user_create_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "email": "example@mail.com",
                "password": "password123",
            }
        },
    )


transaction_get_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "external_id": "txn_123",
                "amount": 500,
                "signature": "abc123",
                "date": "2025-08-14T12:00:00",
                "account_id": 1,
                "user_id": 1
            }
        }
    )

account_get_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True,
        json_schema_extra={"example": {"id": 1, "balance": 1000, "user_id": 1}}
    )