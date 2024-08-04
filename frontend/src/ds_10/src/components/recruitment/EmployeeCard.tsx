import React from 'react'
import { Card, CardContent, CardHeader, CardTitle } from '../ui/Card'
import { GeneralEmployeeType, Skills } from '../dashboards/RecruitmentDashboard'
import { useEmployeeGeneralSkills } from '../../hooks/useEmployeeGeneralSkills'
import { useSelector } from 'react-redux'
import { RootState } from '../../state/store'
import LevelGroupSection from './LevelGroupSection'
import { groupBySkillLevel } from '../../lib/helpers'

const EmployeeCard = ({ selectedEmployeeData, employeeSkills, pickedSkillNames }: { selectedEmployeeData: GeneralEmployeeType, employeeSkills: Skills, pickedSkillNames: string[] }) => {

    const { employee } = useSelector((state: RootState) => state.filters)
    const { groupedGeneralSkillData } = useEmployeeGeneralSkills()

    const skillCategories = ["Языки ", "Предметные области ", "Отрасли ", 'Образование ']

    return (
        <Card className='w-1/2 h-fit'>
            <CardHeader>
                <CardTitle>
                    <div className='flex gap-4 items-end'>
                        <p>{`${selectedEmployeeData?.name}`}</p>
                        <p className='text-sm font-normal'>{selectedEmployeeData?.title}</p>
                    </div>
                </CardTitle>
            </CardHeader>
            <CardContent className='h-full space-y-4'>
                <div className='space-y-1'>
                    <p>{selectedEmployeeData?.department}</p>
                    <p>{`Город: ${selectedEmployeeData?.city}`}</p>
                    <p>{`Почта: ${selectedEmployeeData?.email}`}</p>
                </div>

                {groupedGeneralSkillData &&
                    <div className='space-y-2'>
                        {skillCategories.map((category) => {
                            if (!groupedGeneralSkillData[category]) return
                            return (
                                <div>
                                    <h3 className='font-medium text-lg'>{category}</h3>
                                    <div className='space-y-1'>
                                        {groupedGeneralSkillData[category].map((skill) => {
                                            return (
                                                <p key={`${employee}-${skill.skill}`}>{`${skill.skill} - ${skill.level}`}</p>
                                            )
                                        })}
                                    </div>
                                </div>)
                        })}
                    </div>
                }
                <div className='space-y-3 h-full'>
                    {employee && employeeSkills &&
                        groupBySkillLevel(employeeSkills).map((levelGroup) => {
                            return <LevelGroupSection levelGroup={levelGroup} pickedSkillNames={pickedSkillNames} key={`${employee}-${levelGroup.level}`} />
                        })}
                </div>
            </CardContent>
        </Card>
    )
}

export default EmployeeCard