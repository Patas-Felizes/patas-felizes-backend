import jwt
from backend.config import get_config

def validate_token(token):
    config,_ = get_config()
    try:
        data = jwt.decode(
            token, 
            key=config.SECRET_KEY, 
            algorithms=["HS256", "RS256"],
            verify=True, 
            audience=config.AUDIENCE,
            options={
                "verify_signature": False, # Validação da assinatura
                "verify_iss": False, # Validação de issuer
                "verify_nbf": True, # Verifica se o token está experiado
                "verify_aud": True, # Validação de audiencia
                "verify_exp": True, # Validação do tempo de expiração usando UTC
            }
        )

        return True, {'current_user': data['username']}
    except Exception as err:
        print(err)
        return False, {'message':'token is invalid or expired'}
