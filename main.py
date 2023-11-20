import os
def bubble_sort_ascending(arr):
  n = len(arr)
  for i in range(n):
      for j in range(0, n - i - 1):
          if arr[j] > arr[j + 1]:
              arr[j], arr[j + 1] = arr[j + 1], arr[j]

def bubble_sort_descending(arr):
  n = len(arr)
  for i in range(n):
      for j in range(0, n - i - 1):
          if arr[j] < arr[j + 1]:
              arr[j], arr[j + 1] = arr[j + 1], arr[j]

def input_angka():
  angka = []
  for i in range(5):
      angka.append(int(input(f"Masukkan angka ke-{i + 1}: ")))
  return angka

def main():
  while True:
      angka = input_angka()
      print("Array Inputan:", angka)

      pilihan = input("Pilih pengurutan (asc/desc): ").lower()

      if pilihan == "asc" or pilihan == "ascending":
          bubble_sort_ascending(angka)
          print("Array yang Diurutkan (Ascending):", angka)
      elif pilihan == "desc" or pilihan == "descending":
          bubble_sort_descending(angka)
          print("Array yang Diurutkan (Descending):", angka)
      else:
          print("Pilihan pengurutan tidak valid. Program berakhir.")

      ulangi = input("Apakah Anda ingin menjalankan program lagi? (yes/no): ").lower()
      ("clear")
      if ulangi == "no":
          break
      elif ulangi == "yes":
          angka.clear()
      else:
          print("Pilihan tidak valid. Program berakhir.")
          break