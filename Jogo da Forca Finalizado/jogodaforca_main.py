from jogoDaForca_assets import screenClean, wait, writeScreen, names, wordTips, infoWord, options

screenClean()

writeScreen(f"{'#' * 25}\n{'#' * 7} BEM VINDO {'#' * 7}\n{'#' * 5} JOGO DA FORCA {'#' * 5}\n{'#' * 25}")
wait(2)

names()
wordTips()
infoWord()
options()