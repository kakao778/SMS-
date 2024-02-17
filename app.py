import logging
import requests

# API 정보 설정
API_URL = "https://message.ppurio.com"
# 발신자, 수신자 및 메시지 설정
SENDER = "0319737898"
RECIPIENTS = ["01025824518"]
MESSAGE = "요진타워 비상 연락 문자 발송 테스트입니다."

# 액세스 토큰 직접 입력
ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50IjoiZ0xKSTg0c2VFMXoxeHk1eHEvUFZCdz09IiwiYWxsb3dlZElwTGlzdCI6Ii9iYms0NFFYeG1OK0JVeTFscGVYWmF1aHNiUzQ1SEExQ09JWTErbmVmNzZHK2hlRUhNeWpHcDNQczdaOGwxVHF0TWNsTE4vWVduTjMxYkVTT1l6TERBPT0iLCJyYXRlTGltaXQiOiJ0WmJ4c0ZtSndMZGZiU1RFS2RkWnFRPT0iLCJpYXQiOjE3MDgxMzY1MDgsImV4cCI6MTcwODIyMjkwOCwiaXNzIjoibWVzc2FnZS5wcHVyaW8uY29tIn0.LVfJUDQNCsOycUIeO1WvrWolRbb7H2DXl22c_bOK858"

def send_message(access_token):
    """메시지 발송 함수"""
    url = f"{API_URL}/v1/message"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    # 여러 수신자에게 동일한 메시지를 발송하는 payload 구조
    targets = [{"to": recipient} for recipient in RECIPIENTS]
    payload = {
        "account": "yj0030",  # 뿌리오 계정
        "messageType": "SMS",  # 메시지 타입: SMS
        "content": MESSAGE,  # 메시지 내용
        "from": SENDER,  # 발신번호
        "duplicateFlag": "N",  # 수신번호 중복 허용 여부
        "refKey": "ref_key_example",  # 요청에 부여할 참조 키
        "targetCount": len(RECIPIENTS),  # 수신자 수
        "targets": targets,  # 수신자 목록
    }

    # HTTP POST 요청으로 메시지 발송
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()  # 성공 시 응답 데이터 반환
    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return None

def main():
    """메인 실행 함수"""
    logging.basicConfig(level=logging.INFO)

    # 메시지 발송
    response_data = send_message(ACCESS_TOKEN)
    if response_data and 'messageKey' in response_data:
        logging.info(f"Message successfully sent. Message Key: {response_data['messageKey']}")
    else:
        logging.error("Failed to send the message.")

if __name__ == "__main__":
    main()
