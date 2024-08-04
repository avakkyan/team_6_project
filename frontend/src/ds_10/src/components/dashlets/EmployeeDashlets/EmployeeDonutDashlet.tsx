import React, { useRef } from 'react'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '../../ui/Card';
import { DonutChart, Legend } from '@tremor/react';
import ExportToPNGButton from '../../exportButtons/ExportToPNGButton';
import useFetch from '../../../hooks/useFetch';
import { useFilters } from '../../../hooks/useFilters';
import { defaultDataFormatter } from '../../../lib/formatters';

function groupAndSumByLevel(inputArray) {
    const result = {};

    inputArray.forEach(item => {
        if (result[item.level]) {
            result[item.level] += item.count;
        } else {
            result[item.level] = item.count;
        }
    });

    return Object.keys(result).map(level => ({
        level: level,
        count: result[level]
    }));
}

const EmployeeDonutDashlet = () => {

    const { categoryFilter, skillFilter, employeeFilter, currentLevelFilter, leveledSkillsFilter } = useFilters()

    const { data: levelsData, loading: loadingLevelsData } = useFetch<{ levels_название: string, count: number, 'period_название': string }>({ dimensions: ['levels_название'], measures: ['count(levels_id)', 'period_название'], filters: { ...leveledSkillsFilter, ...categoryFilter, ...skillFilter, ...employeeFilter, ...currentLevelFilter }, queryKey: 'EmployeeDonutData' })
    const finalLevelsData = levelsData ? groupAndSumByLevel(levelsData.filter((el) => el.period_название.length === 4).map((level) => ({ level: level.levels_название, count: level.count }))) : []

    // Refs
    const ref = useRef()

    return (
        <Card className='h-full flex flex-col'>
            <CardHeader className='flex flex-row justify-between items-center'>
                <div>
                    <CardTitle>Соотношение грейдов</CardTitle>
                    <CardDescription>для выбранных фильтров</CardDescription>
                </div>
                <ExportToPNGButton exportRef={ref} />
            </CardHeader>
            <CardContent ref={ref} className='flex flex-col justify-center items-center gap-2 flex-1'>
                <div className='h-56 3xl:h-96 w-full'>
                    <DonutChart
                        data={finalLevelsData}
                        variant='pie'
                        category="count"
                        index="level"
                        colors={['blue', 'lime', 'violet', 'fuchsia', 'teal', 'indigo', 'emerald']}
                        valueFormatter={defaultDataFormatter}
                        className="h-full"
                        showAnimation={true}
                        noDataText='Нет данных'
                        showLabel={false}
                    />
                </div>
                <Legend
                    categories={finalLevelsData.map((el) => el.level)}
                    colors={['blue', 'lime', 'violet', 'fuchsia', 'teal', 'indigo', 'emerald']}
                    className="max-w-xs"
                />

            </CardContent>
        </Card>
    )
}

export default EmployeeDonutDashlet