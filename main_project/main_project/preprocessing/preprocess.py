import pandas as pd

# ----------------------------
# Load GoEmotions Dataset
# ----------------------------
go_df = pd.read_csv("data/raw/goemotions/go_emotions_dataset.csv")

print("=" * 50)
print("GO EMOTIONS DATASET")
print("=" * 50)

print("\nFirst 5 Rows:")
print(go_df.head())

print("\nColumns:")
print(go_df.columns)

print("\nShape:")
print(go_df.shape)

print("\nMissing Values:")
print(go_df.isnull().sum())


# ----------------------------
# Load Student Emotion Dataset
# ----------------------------
student_df = pd.read_csv(
    "data/raw/student_emotion/online_ipe_student_emotion_content_evaluation_dataset.csv"
)

print("\n" + "=" * 50)
print("STUDENT EMOTION DATASET")
print("=" * 50)

print("\nFirst 5 Rows:")
print(student_df.head())

print("\nColumns:")
print(student_df.columns)

print("\nShape:")
print(student_df.shape)

print("\nMissing Values:")
print(student_df.isnull().sum())