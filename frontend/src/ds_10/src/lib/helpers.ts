import { Skills } from "../components/dashboards/RecruitmentDashboard";

export function mergeArrays(array1: { name: string, Рост: number }[], array2: { name: string, Рост: number }[], firstArrayTitle: string, secondArrayTitle: string) {
    const result = [];

    const array2Dict = array2.reduce((acc, item) => {
        acc[item.name] = item.Рост;
        return acc;
    }, {});

    const categoriesSet = new Set();

    array1.forEach(item => {
        categoriesSet.add(item.name);
        result.push({
            name: item.name,
            [secondArrayTitle]: array2Dict[item.name] || 0,
            [firstArrayTitle]: item.Рост,
        });
    });

    array2.forEach(item => {
        if (!categoriesSet.has(item.name)) {
            result.push({
                name: item.name,
                [secondArrayTitle]: item.Рост,
                [firstArrayTitle]: 0,
            });
        }
    });

    return result;
}

export function getNoun(number: number, one: string, two: string, five: string) {
    let n = Math.abs(number);
    n %= 100;
    if (n >= 5 && n <= 20) {
        return five;
    }
    n %= 10;
    if (n === 1) {
        return one;
    }
    if (n >= 2 && n <= 4) {
        return two;
    }
    return five;
}


// Group by skill Level
type SkillsByLevelType = {
    level: string;
    skills: string[];
}[]

type GroupedEmployeeSkillData = {
    [key: string]: Skills
}

export function groupBySkillLevel(employee: GroupedEmployeeSkillData[number]): SkillsByLevelType {
    if (!employee) return []
    const result = [
        { level: 'Использовал в проекте', skills: [] },
        { level: 'Novice', skills: [] },
        { level: 'Junior', skills: [] },
        { level: 'Middle', skills: [] },
        { level: 'Senior', skills: [] },
        { level: 'Expert', skills: [] }
    ]
    for (const [skill, level] of Object.entries(employee)) {
        result[level - 1].skills.push(skill)
    }
    return result.reverse()
}