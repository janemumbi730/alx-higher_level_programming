#include "lists.h"

/**
 * check_cycle - Checks whether linked list has cycles
 * @list: linked list
 * Return: 0 or 1 
 */
int check_cycle(listint_t *list)
{
	listint_t *x, *y;

	if (list == NULL || list->next == NULL)
		return (0);

	x = list->next;
	y = list->next->next;

	while (x && y && y->next)
	{
		if (x == y)
			return (1);

		x = x->next;
		y = y->next->next;
	}
	return (0);
}
