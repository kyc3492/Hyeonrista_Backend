import logging
import boto3
from botocore.client import Config
from botocore.exceptions import ClientError
from S3_config import AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY, AWS_S3_BUCKET_REGION, AWS_S3_BUCKET_NAME

def s3_connection():
    '''
    s3 bucket에 연결
    :return: 연결된 s3 객체
    '''
    try:
        s3 = boto3.client(
            service_name='s3',
            region_name=AWS_S3_BUCKET_REGION,
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            config=Config(signature_version='s3v4')
        )
    except Exception as e:
        print(e)
        exit("ERROR_S3_CONNECTION_FAILED")
    else:
        print("s3 bucket connected!")
        response = s3.list_buckets() # bucket 목록
        print(response)
        return s3

def s3_get_object(s3, bucket, object_name, file_name):
    '''
    s3 bucket에서 지정 파일 다운로드
    :param s3: 연결된 s3 객체(boto3 client)
    :param bucket: 버킷명
    :param object_name: s3에 저장된 object 명
    :param file_name: 저장할 파일 명(path)
    :return: 성공 시 True, 실패 시 False 반환
    '''
    try:
        s3.download_file(bucket, object_name, file_name)
    except Exception as e:
        print(e)
        return False
    return True

def create_presigned_url(object_name):
    """Generate a presigned URL to share an S3 object

    :param bucket_name: string
    :param object_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """
    s3 = s3_connection()
    bucket = AWS_S3_BUCKET_NAME

    # Generate a presigned URL for the S3 object
    try:
        response = s3.generate_presigned_url('get_object',
                                            Params={'Bucket': bucket,
                                                    'Key': object_name}
                                            )
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    return response

'''url = create_presigned_url(s3_connection(), AWS_S3_BUCKET_NAME, "hyeonrista/cafe1.png")
print("cafe1 : " + url)

url = create_presigned_url(s3_connection(), AWS_S3_BUCKET_NAME, "hyeonrista/cafe2.png")
print("cafe2 : " + url)

url = create_presigned_url(s3_connection(), AWS_S3_BUCKET_NAME, "hyeonrista/cafe3.png")
print("cafe3 : " + url)

url = create_presigned_url(s3_connection(), AWS_S3_BUCKET_NAME, "hyeonrista/cafe4.png")
print("cafe4 : " + url)'''