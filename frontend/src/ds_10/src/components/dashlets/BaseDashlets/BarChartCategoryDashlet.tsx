import React, { useEffect, useRef, useState } from 'react'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '../../ui/Card';
import { BarChart } from '@tremor/react';
import ExportToPNGButton from '../../exportButtons/ExportToPNGButton';
import useFetch from '../../../hooks/useFetch';
import { useFilters } from '../../../hooks/useFilters';
import { mergeArrays } from '../../../lib/helpers';
import { shortCategoryVariants } from '../../../lib/data';
import { defaultDataFormatter } from '../../../lib/formatters';

const BarChartCategoryDashlet = () => {

    const ref = useRef()

    const { leveledSkillsFilter, currentPeriodFilter, previousPeriodFilter, departmentFilter, currentPeriod, previousPeriod, filtersAreReady } = useFilters()

    // Category Fetching
    const { data: currentCategoryData, loading: loadingCurrentCategoryData } = useFetch<{ category_know_название: string, growth: number }>({ dimensions: ['category_know_название'], measures: ['category_know_название', 'sum(growth)'], filters: { ...leveledSkillsFilter, ...currentPeriodFilter, ...departmentFilter }, filtersAreReady, queryKey: 'BarChartCategoryData' })
    const { data: previousCategoryData, loading: loadingPreviousCategoryData } = useFetch<{ category_know_название: string, growth: number }>({ dimensions: ['category_know_название'], measures: ['category_know_название', 'sum(growth)'], filters: { ...leveledSkillsFilter, ...previousPeriodFilter, ...departmentFilter }, filtersAreReady, queryKey: 'BarChartCategoryData' })

    const [categoryData, setCategoryData] = useState([])

    useEffect(() => {
        if (!loadingCurrentCategoryData && !loadingPreviousCategoryData) {
            const finalCurrentData = currentCategoryData ? currentCategoryData.map((skill) => ({ name: shortCategoryVariants.get(skill.category_know_название), Рост: skill.growth })).sort((a, b) => b.Рост - a.Рост) : []
            const finalPreviousData = previousCategoryData ? previousCategoryData.map((skill) => ({ name: shortCategoryVariants.get(skill.category_know_название), Рост: skill.growth })).sort((a, b) => b.Рост - a.Рост) : []
            setCategoryData(mergeArrays(finalCurrentData, finalPreviousData, currentPeriod, previousPeriod))
        }
    }, [currentCategoryData, previousCategoryData])


    return (
        <Card className='h-full flex flex-col'>
            <CardHeader className='flex flex-row justify-between items-center'>
                <div>
                    <CardTitle>Области знаний</CardTitle>
                    <CardDescription>сравнительный анализ по периодам</CardDescription>
                </div>
                <ExportToPNGButton exportRef={ref} />
            </CardHeader>
            <CardContent ref={ref} className='flex-1'>
                <BarChart
                    data={categoryData}
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

export default BarChartCategoryDashlet