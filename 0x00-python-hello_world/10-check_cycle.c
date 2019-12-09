#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - check if the linked list is a cycle.
 * @list: Address of each node
 * Return: 1 cycle, 0 no cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp;

	if (list)
	{
		while (list != NULL)
		{
			tmp = list;
			list = list->next;
			if (tmp <= list)
				return (1);
		}
		return (0);
	}
	return (0);
}
