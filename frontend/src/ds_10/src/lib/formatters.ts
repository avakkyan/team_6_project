export const defaultDataFormatter = (number: number) => {
    return Intl.NumberFormat('ru').format(number).toString()
}
