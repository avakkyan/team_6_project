import React, { useEffect, useRef, useState } from 'react'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '../../ui/Card';
import { BarChart } from '@tremor/react';
import ExportToPNGButton from '../../exportButtons/ExportToPNGButton';
import useFetch from '../../../hooks/useFetch';
import { useFilters } from '../../../hooks/useFilters';
import { useSelector } from 'react-redux';
import { RootState } from '../../../state/store';
import { mergeArrays } from '../../../lib/helpers';
import { defaultDataFormatter } from '../../../lib/formatters';

const BarChartSkillDashlet = () => {

    const ref = useRef()

    const { category } = useSelector((state: RootState) => state.filters)

    const { leveledSkillsFilter, currentPeriodFilter, previousPeriodFilter, departmentFilter, categoryFilter, currentPeriod, previousPeriod, filtersAreReady } = useFilters()

    // Knowledge Fetching
    const { data: currentSkillsData, loading: loadingCurrentSkillsData } = useFetch<{ knows_название: string, growth: number }>({ dimensions: ['knows_название'], measures: ['knows_название', 'sum(growth)'], filters: { ...leveledSkillsFilter, ...currentPeriodFilter, ...departmentFilter, ...categoryFilter }, filtersAreReady, queryKey: 'BarChartSkill' })
    const { data: previousSkillsData, loading: loadingPreviousSkillsData } = useFetch<{ knows_название: string, growth: number }>({ dimensions: ['knows_название'], measures: ['knows_название', 'sum(growth)'], filters: { ...leveledSkillsFilter, ...previousPeriodFilter, ...departmentFilter, ...categoryFilter }, filtersAreReady, queryKey: 'BarChartSkill' })

    const [skillData, setSkillData] = useState([])

    useEffect(() => {
        if (!loadingCurrentSkillsData && !loadingPreviousSkillsData) {
            const finalCurrentSkillsData = currentSkillsData ? currentSkillsData.map((skill) => ({ name: skill.knows_название, Рост: skill.growth })).sort((a, b) => b.Рост - a.Рост) : []
            const finalPreviousSkillsData = previousSkillsData ? previousSkillsData.map((skill) => ({ name: skill.knows_название, Рост: skill.growth })).sort((a, b) => b.Рост - a.Рост) : []
            setSkillData(mergeArrays(finalCurrentSkillsData, finalPreviousSkillsData, currentPeriod, previousPeriod))
        }
    }, [currentSkillsData, previousSkillsData])

    return (
        <Card className='h-full flex flex-col'>
            <CardHeader className='flex flex-row justify-between items-center'>
                <div>
                    <CardTitle>{category}</CardTitle>
                    <CardDescription>сравнительный анализ по периодам</CardDescription>
                </div>
                <ExportToPNGButton exportRef={ref} />
            </CardHeader>
            <CardContent ref={ref} className='flex-1'>
                <BarChart
                    data={skillData}
                    index="name"
                    categories={[previousPeriod, currentPeriod]}
                    colors={['blue', 'rose']}
                    valueFormatter={defaultDataFormatter}
                    yAxisWidth={48}
                    showYAxis={true}
                    yAxisLabel='Грейды'
                    className='text-sm h-full'
                    noDataText='Нет данных'
                    showAnimation={true}
                />
            </CardContent>
        </Card>
    )
}

export default BarChartSkillDashlet