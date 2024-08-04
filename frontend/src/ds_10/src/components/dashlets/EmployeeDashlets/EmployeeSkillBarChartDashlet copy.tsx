import React, { useEffect, useRef, useState } from 'react'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '../../ui/Card';
import { BarChart } from '@tremor/react';
import { cn } from '../../../lib/utils';
import ExportToPNGButton from '../../exportButtons/ExportToPNGButton';
import useFetch from '../../../hooks/useFetch';
import { useFilters } from '../../../hooks/useFilters';
import { useSelector } from 'react-redux';
import { RootState } from '../../../state/store';
import { defaultDataFormatter } from '../../../lib/formatters';

function mergeArrays(array1: { knows_название: string, sum: number, подразделения: string }[], array2: { knows_название: string, sum: number, "User ID": number }[], firstArrayTitle: string, secondArrayTitle: string) {
    const result = [];

    array1 = array1.sort((a, b) => b.sum - a.sum)

    const array2Dict = array2.reduce((acc, item) => {
        acc[item.knows_название] = +(item.sum / item['User ID']).toFixed(1);
        return acc;
    }, {});

    array1.forEach(item => {
        result.push({
            name: item.knows_название,
            [secondArrayTitle]: array2Dict[item.knows_название] || 0,
            [firstArrayTitle]: item.sum,
        });
    });

    return result
}

const EmployeeSkillBarChartDashlet = () => {

    const ref = useRef()

    const { category } = useSelector((state: RootState) => state.filters)
    const { leveledSkillsFilter, categoryFilter, employeeFilter, currentLevelFilter, yearPeriodsFilter } = useFilters()
    const [employeeDepartment, setEmployeeDepartment] = useState('')

    // Knowledge Fetching
    const { data: currentSkillsData, loading: loadingCurrentSkillsData } = useFetch<{ knows_название: string, sum: number, подразделения: string }>({ dimensions: ['knows_название'], measures: ['sum(levels_n_level)', 'подразделения'], filters: { ...leveledSkillsFilter, ...employeeFilter, ...categoryFilter, ...currentLevelFilter, ...yearPeriodsFilter }, queryKey: 'EmployeeBarChartSkill' })

    // Fetching Average Department value
    const { data: sumByDepartmentData, loading: loadingSumByDepartmentData } = useFetch<{ knows_название: string, sum: number, "User ID": number }>({ dimensions: ['knows_название'], measures: ['sum(levels_n_level)', 'uniq("User ID")'], filters: { ...leveledSkillsFilter, ...currentLevelFilter, ...categoryFilter, ...yearPeriodsFilter, 'подразделения': ['=', employeeDepartment] }, filtersAreReady: !!employeeDepartment, queryKey: 'AverageDepartmentSkills' })

    const [finalData, setFinalData] = useState([])

    useEffect(() => {
        if (sumByDepartmentData && currentSkillsData) {
            if (currentSkillsData.length) {
                setFinalData(mergeArrays(currentSkillsData, sumByDepartmentData, 'Сотрудник', 'Среднее по отделу'))
            }
            else {
                setFinalData([])
            }
        }
    }, [sumByDepartmentData, currentSkillsData])

    useEffect(() => {
        if (currentSkillsData?.length) {
            setEmployeeDepartment(currentSkillsData[0].подразделения)
        }
    }, [currentSkillsData])


    return (
        <Card className='flex flex-col h-full'>
            <CardHeader className='flex flex-row justify-between items-center'>
                <div>
                    <CardTitle>{category}</CardTitle>
                    <CardDescription>сравнительный анализ с подразделением</CardDescription>
                </div>
                <ExportToPNGButton exportRef={ref} />
            </CardHeader>
            <CardContent ref={ref} className='flex flex-1 gap-2'>
                <div className={cn('visible flex flex-col justify-between pt-[2.1rem] h-[67.5%]', finalData.length === 0 && 'invisible')}>
                    <p>Expert</p>
                    <p>Senior</p>
                    <p>Middle</p>
                    <p>Junior</p>
                    <p>Novice</p>
                </div>
                <BarChart
                    data={finalData}
                    index="name"
                    categories={["Среднее по отделу", "Сотрудник"]}
                    colors={['blue', 'rose']}
                    valueFormatter={defaultDataFormatter}
                    yAxisWidth={48}
                    showYAxis={false}
                    minValue={0}
                    maxValue={6}
                    className='text-sm h-full'
                    noDataText='Нет данных'
                    showAnimation={true}
                />
            </CardContent>
        </Card>
    )
}

export default EmployeeSkillBarChartDashlet