APPLICATION_NAME = "soundbyte"

DEFAULT_SEPARATOR = '-'

DOWNLOAD_BASE_FILE_NAME = f"{APPLICATION_NAME}.media.download"
METADATA_FILE_TYPE = "info.json"
AUDIO_FILE_TYPE = "wav"

WORK_ROOT = f"C:\\Users\\John Hart\\Desktop\\{APPLICATION_NAME}"
TEMP_ROOT = f"{WORK_ROOT}\\temp"
CACHE_ROOT = f"{WORK_ROOT}\\cache"
EXPORT_ROOT = f"{WORK_ROOT}\\export"

LOG_DEBUG = True
LOG_WARNING = True
LOG_ERROR = True
LOG_TO_CONSOLE = True

LOG_ROOT = f"{WORK_ROOT}\\log"
LOG_FILE_TYPE = "log"
LOG_FILE_NAME = f"{LOG_ROOT}\\{APPLICATION_NAME}.{LOG_FILE_TYPE}"

DEFAULT_EXTERNAL_DOWNLOADER = "aria2c"
DEFAULT_FRAME_RATE = 44100

DEFAULT_CLIPS = 10
DEFAULT_DETECTION_CHUNK_SIZE_MILISECONDS = 10
DEFAULT_LOW_VOLUME_THRESHOLD_DECIBELS = -20.0
DEFAULT_VOLUME_DRIFT_DECIBELS = 0.1
DEFAULT_CLIP_SIZE_MILISECONDS = 9000
DEFAULT_BEAT_COUNT = 4
DEFAULT_ATTACK_MILISECONDS = 50
DEFAULT_PAD_DURATION_MILISECONDS = 250

DEFAULT_FADE_IN_MILISECONDS = 500
DEFAULT_FADE_OUT_MILISECONDS = 500

MAXIMUM_CLIP_SIZE_MILISECONDS = 27000
MAXIMUM_SAMPLES = 24 * 60 * 60 * DEFAULT_FRAME_RATE
