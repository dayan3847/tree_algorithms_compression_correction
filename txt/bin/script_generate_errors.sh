#!/bin/bash

(
  # Change Directory to root
  cd "$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)" &&
    (
      [ -e ./injectError ] || gcc -Wall -g -o injectError injectError.c

      [ -e ./Salida.bin ] && rm Salida.bin
      [ -e ./ReporteErrores.txt ] && rm ReporteErrores.txt

      [ -e ./Entrada.bin ] && ./injectError 0.125
    )
)
