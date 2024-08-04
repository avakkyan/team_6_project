import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
    return twMerge(clsx(inputs))
}

export function getCurrentPeriod() {
    return {
        halfyear: 'both',
        year: new Date().getFullYear().toString()
    }
}

export function groupByAndSum(inputArray) {
    const result = {};

    inputArray.forEach(item => {
        if (result[item.name]) {
            result[item.name] += item.Уровень;
        } else {
            result[item.name] = item.Уровень;
        }
    });

    return Object.keys(result).map(name => ({
        name: name,
        Уровень: result[name]
    }));
}